import os
import glob
import numpy as np
from khumeia.data.item import SatelliteImage


class Collection(object):
    """
    A collection is a list of items with a name
    """

    def __init__(self, name, items):
        """

        Args:
            name:
            items:
        """
        self.name = name
        self.items = items

    def __len__(self):
        """

        Returns:

        """
        return len(self.items)

    def __iter__(self):
        """

        Returns:

        """
        for p in self.items:
            yield p

    def __getitem__(self, item):
        """

        Args:
            item:

        Returns:

        """
        return self.items[item]


class SatelliteImagesCollection(Collection):
    """
    SatelliteImageCollection for aircraft detection
    """

    def __init(self, name, items):
        """

        Args:
            name:
            items:

        Returns:

        """
        super(SatelliteImagesCollection, self).__init__(name=name, items=items)

    def __str__(self):
        s = ""
        s += "--- Item collection ---\n"
        s += "collection_id: {}\n".format(self.name)
        s += "Number of items: {}\n".format(len(self))
        for item in self.items:
            s += str(item)
        return s

    @classmethod
    def from_path(cls, path=None):
        """

        Args:
            path:

        Returns:

        """
        assert path is not None, "Please set folder variable, likely ./data/raw/trainval/"
        items = []
        list_images = glob.glob(os.path.join(path, "*.jpg"))
        collection_name = os.path.dirname(list_images[0]).split("/")[-1]

        for image_file in list_images:
            image_id = os.path.splitext(os.path.basename(image_file))[0]
            item = SatelliteImage.from_image_id_and_path(image_id, path=path)
            # Read the when initialising to put data into cache
            assert isinstance(item.image, np.ndarray)
            assert isinstance(item.labels, list)
            items.append(item)

        items = sorted(items, key=lambda item: item.key)

        return cls(collection_name, items)
