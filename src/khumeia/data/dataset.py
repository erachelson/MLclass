import os
import shutil
from tqdm.autonotebook import tqdm

from khumeia.utils import io, list_utils
from khumeia import LOGGER
from khumeia.data.sampler import TilesSampler


class TilesDataset(object):
    """
    A tiles dataset is a container for "tiles" on items
    It is used to apply sliding windows on full images to generate candidates
    then sample
    then output data to keras format
    """

    def __init__(self, items):
        """

        Args:
            items:
        """
        self.items = items
        self.sliding_windows = list([])
        self.tiles_samplers = list([])
        self.candidate_tiles = list([])
        self.sampled_tiles = list([])
        self.found_labels = list([])

    def generate_candidates_tiles(self, sliding_windows):
        """

        Args:
            sliding_windows(list[khumeia.data.sliding_window.SlidingWindow]|khumeia.data.sliding_window.SlidingWindow):

        Returns:

        """
        if not isinstance(sliding_windows, (list, tuple)):
            sliding_windows = [sliding_windows]
        self.sliding_windows = sliding_windows

        sliding_windows = self.sliding_windows
        items = self.items

        LOGGER.info("Generating a pool of candidates tiles")

        candidate_tiles = []
        for sliding_window in tqdm(sliding_windows, position=0, desc="Applying slider"):
            for item in tqdm(items, position=1, desc="On item"):
                candidate_tiles.extend(sliding_window.get_tiles_for_item(item))

        LOGGER.info("Candidates tiles generated ! Now sample them using Dataset.sample_tiles_from_candidates")

        self.candidate_tiles = list(set(candidate_tiles))
        self.found_labels = list_utils.get_labels_in_list(self.candidate_tiles)

        # Initialise sampled tiles by default (copy candidate tiles)
        self.sampled_tiles = self.candidate_tiles[:]

    def sample_tiles_from_candidates(self, tiles_samplers):
        """

        Args:
            tiles_samplers(list[TilesSampler]|TilesSampler):

        Returns:

        """
        sampled_tiles = []

        if not isinstance(tiles_samplers, (list, tuple)):
            tiles_samplers = [tiles_samplers]
        self.tiles_samplers = tiles_samplers

        LOGGER.info("Sampling tiles")
        for tile_sample in tqdm(self.tiles_samplers, desc="Sampling tiles"):
            sampled_tiles.extend(tile_sample.sample_tiles_from_candidates(self.candidate_tiles))

        LOGGER.info("Tiles sampled, now generate the dataset using Dataset.generate_tiles_dataset")

        self.sampled_tiles = sampled_tiles

    def generate_tiles_dataset(self, output_dir=None, save_format="jpg", remove_first=True):
        """

        Args:
            output_dir:
            save_format: "jpg"
            remove_first(bool): erase output dir first?

        Returns:

        """
        LOGGER.info("Generating a dataset of tiles at location {}".format(output_dir))

        for label in self.found_labels:
            if remove_first:
                shutil.rmtree(os.path.join(output_dir, label))
            if not os.path.exists(os.path.join(output_dir, label)):
                os.makedirs(os.path.join(output_dir, label))

        def _generate_tiles(item, tiles):
            image = item.image
            tiles = list_utils.filter_tiles_by_item(tiles, item.key)
            for tile in tiles:
                tile_data = tile.get_data(image)
                tile_label = tile.label
                tile_basename = "{}_{}.{}".format(item.key, tile.key, save_format)
                io.imsave(os.path.join(output_dir, tile_label, tile_basename), tile_data)

        items = self.items
        sampled_tiles = self.sampled_tiles

        LOGGER.info("Dumping tiles to {}".format(output_dir))

        for item in tqdm(items, desc="Saving tiles to {}".format(output_dir)):
            _generate_tiles(item, sampled_tiles)

    def __str__(self):
        s = ""
        s += "--- TilesDataset ---\n"
        s += "Found labels {}".format(self.found_labels)
        s += "\n- Sliding windows:\n"
        for sliding_window in self.sliding_windows:
            s += str(sliding_window) + "\n"
        s += "\n- Samplers:\n"
        for sampler in self.tiles_samplers:
            s += str(sampler) + "\n"
        s += "\n- Candidate tiles:\n"
        for item in self.items:
            nb_tiles = len(list_utils.filter_tiles_by_item(self.candidate_tiles, item.key))
            s += "Item {}: {} rois\n".format(item.key, nb_tiles)
            for label in self.found_labels:
                nb_tiles = len(list_utils.filter_tiles_by_item_by_label(self.candidate_tiles, item.key, label))
                s += "Item {}: Label {}: {} rois\n".format(item.key, label, nb_tiles)
        s += "\n- Sampled tiles:\n"
        for item in self.items:
            nb_tiles = len(list_utils.filter_tiles_by_item(self.sampled_tiles, item.key))
            s += "Item {}: {} rois\n".format(item.key, nb_tiles)
            for label in self.found_labels:
                nb_tiles = len(list_utils.filter_tiles_by_item_by_label(self.sampled_tiles, item.key, label))
                s += "Item {}: Label {}: {} rois\n".format(item.key, label, nb_tiles)

        return s
