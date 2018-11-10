import random


class Predictor(object):
    """
    A predictor is simply a wrapper over a model to predict aircraft or background
    FN predict_on_tile should return either [aircraft or background]
    use __init__ to load your model !

    It supports batching if your class has an attribute batch_size
    """

    def predict_on_tile(self, tile_data):
        """
        receives a numpy array, returns the label
        Args:
            tile_data(np.ndarray):

        Returns:
            "aircraft" or "background"

        """
        raise NotImplementedError

    def predict_on_tiles(self, tiles_data):
        """
        If you want to implement batching
        Args:
            tiles_data(list[np.ndarray]): A list of images

        Returns:
            A list of labels "aircraft" or "background"

        """
        raise NotImplementedError


class DemoPredictor(Predictor):
    """
    Dummy predictor randomly returning aircraft or background
    """

    def __init__(self, threshold=0.9, batch_size=128):
        self.threshold = threshold
        self.batch_size = batch_size
        self.model = lambda x: "aircraft" if random.random > threshold else "background"

    def predict_on_tile(self, tile_data):
        return self.model(tile_data)

    def predict_on_tiles(self, tiles_data):
        return [self.model(tile_data) for tile_data in tiles_data]
