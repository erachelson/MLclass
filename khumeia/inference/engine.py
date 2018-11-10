from khumeia import LOGGER
from tqdm.autonotebook import tqdm
from khumeia.roi.tile import PredictionTile


class InferenceEngine(object):
    """

    """

    def __init__(self, items):
        self.items = items

    @staticmethod
    def predict_on_item(item, predictor=None, sliding_windows=None):
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
            for batch in tqdm(batches, desc="Predicting on batch"):
                batch_results = predictor.predict_on_tiles(batch)
                for i, tile in enumerate(batch):
                    tiles_results.append(PredictionTile.from_labelled_tile_and_prediction(tile, batch_results[i]))
        else:
            for tile in tqdm(tiles_to_predict, desc="Predicting on tile"):
                prediction = predictor.predict_on_tile(tile.get_data(image))
                tiles_results.append(PredictionTile.from_labelled_tile_and_prediction(tile, prediction))

        return tiles_results

    def predict_on_items(self, predictor=None, sliding_windows=None):
        for item in self.items:
            self.predict_on_item(item, predictor=predictor, sliding_windows=sliding_windows)
