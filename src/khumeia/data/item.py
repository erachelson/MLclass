import os
import khumeia.utils.io
from khumeia import LOGGER


class Item(object):
    """
    An item is a container
    """

    @property
    def key(self):
        """

        Returns:

        """
        raise NotImplementedError


class SatelliteImage(Item):
    """
    Contains image id, image file and label file
    Contains read_image and read labels as property (cached via joblib to avoid loading the same image n times and to avoid ram overflow)
    """
    def __init__(self, image_id, image_file, label_file):
        """

        Args:
            image_id:
            image_file:
            label_file:
        """
        self.image_id = image_id
        self.image_file = image_file
        self.label_file = label_file

    @classmethod
    def from_image_id_and_path(cls, image_id, path=None):
        """

        Args:
            image_id:
            path:

        Returns:

        """
        image_file = os.path.join(path, "{}.jpg".format(image_id))
        label_file = os.path.join(path, "{}.json".format(image_id))

        return cls(image_id=image_id, image_file=image_file, label_file=label_file)

    @property
    def key(self):
        """

        Returns:

        """
        return self.image_id

    @property
    def image(self):
        """

        Returns:

        """
        image = khumeia.utils.io.imread(self.image_file)
        return image

    @property
    def labels(self):
        """

        Returns:

        """
        return khumeia.utils.io.read_aircraft_labels(self.label_file)

    @property
    def shape(self):
        """

        Returns:

        """
        return self.image.shape

    def __str__(self):
        s = "--- Item description ---\n"
        s += "image_id: {}\n".format(self.image_id)
        s += "image_file: {}\n".format(self.image_file)
        s += "label_file: {}\n".format(self.label_file)
        s += "image_shape: {}\n".format(self.shape)
        s += "number of labels: {}\n".format(len(self.labels))
        return s
