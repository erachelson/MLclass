import os
import json
import glob
import khumeia.utils.io
import numpy as np
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
    Contains the necessary information to define a satellite images
    Contains image id, image file and label file
    Contains image and labels as properties (cached via joblib to avoid loading the same image n times and to avoid ram overflow)
    The labels are automatically parsed as BoundingBoxes
    """

    def __init__(self, image_id, image_file, label_file):
        """

        Args:
            image_id: the image identifier (generally the filename...)
            image_file: path to the .jpg image file
            label_file: path to the .json label file
        """
        self.image_id = image_id
        self.image_file = image_file
        self.label_file = label_file

    @classmethod
    def list_items_from_path(cls, path=None):
        """
        Get a list of Satellite Images items from path

        Args:
            path: folder where to look

        Returns:
            list(SatelliteImageItem):
        """
        assert path is not None, "Please set folder variable, likely ${TP_ISAE_DATA}/raw/trainval/"

        LOGGER.info("Looking in {}".format(path))
        items = []
        list_images = glob.glob(os.path.join(path, "*.jpg"))

        for image_file in list_images:
            image_id = os.path.splitext(os.path.basename(image_file))[0]
            item = SatelliteImage.from_image_id_and_path(image_id, path=path)
            # Read the when initialising to put data into cache
            assert isinstance(item.image, np.ndarray)
            assert isinstance(item.labels, list)
            items.append(item)

        items = list(sorted(items, key=lambda item: item.key))

        return items

    @classmethod
    def from_image_id_and_path(cls, image_id, path=None):
        """

        Args:
            image_id: the filename
            path: the root directory to parse when looking for .jpg and .json files

        Returns:

        """
        image_file = os.path.join(path, "{}.jpg".format(image_id))
        label_file = os.path.join(path, "{}.json".format(image_id))

        return cls(image_id=image_id, image_file=image_file, label_file=label_file)

    @property
    def key(self):
        """
        An unique identifier of the Item class used to for matching

        Returns:
            str: the image_id

        """
        return self.image_id

    @property
    def image(self):
        """
        Read image data (wrapper around skimage.imread)
        Returns:
            np.ndarray: the image data as a int8 (h,w,3) np.ndarray
        """
        image = khumeia.utils.io.imread(self.image_file)
        return image

    @property
    def labels(self):
        """
        Get the labels of a satellite image (load json and decode labels)

        Returns:
            list(Groundtruth): A list of bounding boxes corresponding to the labels

        """
        return khumeia.utils.io.read_aircraft_labels(self.label_file)

    @property
    def shape(self):
        """
        Get the shape of the array (wrapper around self.image.shape)

        Returns:
            tuple: h,w,c

        """
        return self.image.shape

    def __str__(self):
        d = dict()
        d['class'] = self.__class__.__name__
        d['image_shape'] = self.shape
        d['nb_labels'] = len(self.labels)
        d.update(self.__dict__)
        return json.dumps(d, indent=4)

    def __repr__(self):
        return self.__str__()
