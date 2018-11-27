from khumeia import LOGGER
from tqdm.autonotebook import tqdm
from khumeia.roi.tile import PredictionTile
from khumeia.inference.predictor import Predictor


class InferenceEngine(object):
    """
    Classe qui se comporte comme `Dataset` mais donne accès à la prédiction sur chaque tuile à l'aide d'une fenêtre glissante

    ![](https://cdn-images-1.medium.com/max/1600/1*uLk0eLyS8sYCqXTgEYcO6w.png)
    """

    def __init__(self, items):
        self.items = items

    @staticmethod
    def predict_on_item(item, predictor=None, sliding_windows=None):
        """

        Args:
            item(SatelliteImage): the item on which to apply the prediction
            predictor(Predictor): A Predictor object that encapsulates our model
            sliding_windows(SlidingWindow): The sliding window used to generate candidates

        Returns:

        """
        if not isinstance(sliding_windows, (list, tuple)):
            sliding_windows = [sliding_windows]
        LOGGER.info("Generating tiles to predict")
        tiles_to_predict = []
        for sliding_window in tqdm(sliding_windows, position=0, desc="Applying slider"):
            tiles_to_predict.extend(sliding_window.get_tiles_for_item(item))

        tiles_to_predict = list(set(tiles_to_predict))
        LOGGER.info("Generating predicting on item {} with {} tiles".format(item.key, len(tiles_to_predict)))

        image = item.image

        tiles_results = []
        if hasattr(predictor, "batch_size") and predictor.batch_size > 1:
            batches = [
                tiles_to_predict[i:i + predictor.batch_size]
                for i in range(0, len(tiles_to_predict), predictor.batch_size)
            ]
            for batch in tqdm(
                    batches, desc="Calling .predict_on_batch() with batch_size {}".format(predictor.batch_size)):
                batch_data = [tile.get_data(image) for tile in batch]
                batch_results = predictor.predict_on_batch(batch_data)
                for i, tile in enumerate(batch):
                    tiles_results.append(PredictionTile.from_labelled_tile_and_prediction(tile, batch_results[i]))
        else:
            for tile in tqdm(tiles_to_predict, desc="Calling .predict() with one tile"):
                prediction = predictor.predict(tile.get_data(image))
                tiles_results.append(PredictionTile.from_labelled_tile_and_prediction(tile, prediction))

        return tiles_results

    def predict_on_items(self, predictor=None, sliding_windows=None):
        """
            Apply predictor + sliding window on all items in self.items
        Args:
            predictor(Predictor): A Predictor object that encapsulates our model
            sliding_windows(SlidingWindow): The sliding window used to generate candidates

        Returns:
            A list of PredictionTile (Tile + predicted_label + groundtruth label)

        """
        for item in self.items:
            self.predict_on_item(item, predictor=predictor, sliding_windows=sliding_windows)
