import json
import random
import numpy as np
from khumeia import LOGGER
from khumeia.utils import list_utils
from khumeia.roi.tile import Tile

random.seed(2018)
np.random.seed(2018)


class TilesSampler(object):
    """
    A Sampler takes as input a list of tiles and outputs a transformed list of tiles, after application of a sampling
    logic. See https://en.wikipedia.org/wiki/Sampling_(statistics)

    Writing our own sampler:

    You have to write `sample_tiles_from_candidates(self, candidate_tiles)`

    Example:
        make use of the list filters utils

        ```python
        from khumeia.utils import list_utils

            def sample_tiles_from_candidates(self, candidate_tiles):
        sampled_tiles = []
        item_keys = list_utils.get_items_in_list(candidate_tiles)

        for item_key in item_keys:
            candidate_tiles_ = list_utils.filter_tiles_by_item(candidate_tiles, item_key)
            if self.target_label is not None:
                candidate_tiles_ = list_utils.filter_tiles_by_label(candidate_tiles_, self.target_label)

            nb_tiles_max = int((self.nb_tiles_max or len(candidate_tiles_)) / len(item_keys))

            sampled_tiles.extend(self._sample_n_tiles_from_list(candidate_tiles_, nb_tiles_max))

        return sampled_tiles
        ```

    """

    def __init__(self, with_replacement=False, shuffle=True):
        """

        Args:
            with_replacement (bool):  We will sample with replacement
            shuffle (bool): Shuffle the input list of tiles first
        """
        self.with_replacement = with_replacement
        self.shuffle = shuffle

    def _sample_n_tiles_from_list(self, tiles, nb_tiles_max):
        """
        Select `nb_tiles_max` tiles from the list `tiles`. If `with_replacement`, then selects exactly this amount,
        else selects min(len(tiles),nb_tiles_max))
        If shuffle: shuffle the list of tiles
        Args:
            tiles(list[Tile]): List of tiles to sample from
            nb_tiles_max (int): Nb of tiles max to sample

        Returns:
            The sampled list of tiles
        """
        nb_candidates = len(tiles)
        tiles_idx = list(range(nb_candidates))

        if not self.with_replacement:
            nb_tiles_max = min(nb_candidates, nb_tiles_max)

        if self.shuffle:
            random.shuffle(tiles_idx)

        return [tiles[tiles_idx[idx % nb_candidates]] for idx in range(nb_tiles_max)]

    def sample_tiles_from_candidates(self, candidate_tiles):
        """
        Apply the sampling logic of this class to a list of `candidates`
        Args:
            candidate_tiles(list[Tiles]): List of regions of interest to apply the sampler on

        Returns:
            list[Tiles]: Sampled list
        """
        raise NotImplementedError

    def __str__(self):
        d = dict()
        d['class'] = self.__class__.__name__
        d.update(self.__dict__)
        return json.dumps(d, indent=4)


class RandomSampler(TilesSampler):
    """
    Samples randomly at most `nb_tiles_max` tiles from the candidates pool
    If with_replacement is activated, exactly nb_tiles_max
    Note: you can target a specific label for extracting only n images from this label
    This is useful if you want to stratify manually instead of using more complex samplers
    """

    def __init__(self, nb_tiles_max=None, with_replacement=False, shuffle=True, target_label=None):
        """

        Args:
            nb_tiles_max(int):
            target_label(str|None):  Allow targeting a specific label
        """
        super(RandomSampler, self).__init__(with_replacement=with_replacement, shuffle=shuffle)
        self.nb_tiles_max = nb_tiles_max
        self.with_replacement = with_replacement
        self.target_label = target_label

    def sample_tiles_from_candidates(self, candidate_tiles):
        """
        Apply the sampling logic of this class to a list of `candidates`
        Args:
            candidate_tiles(list[Tiles]): List of regions of interest to apply the sampler on

        Returns:
            list[Tiles]: Sampled list
        """
        LOGGER.info("Sampling")

        if self.target_label is not None:
            candidate_tiles = list_utils.filter_tiles_by_label(candidate_tiles, self.target_label)

        nb_tiles_max = self.nb_tiles_max or len(candidate_tiles)

        return self._sample_n_tiles_from_list(candidate_tiles, nb_tiles_max)


class RandomPerItemSampler(RandomSampler):
    """
    Samples randomly at most `nb_tiles_max` tiles from the candidates pool
    If with_replacement is activated, exactly nb_tiles_max
    Ensures that at most `nb_tiles_max/nb_items` tiles are sampled per item
    Note: you can target a specific label for extracting only n tiles from this label.
    This is useful if you want to stratify manually instead of using more complex samplers
    """

    def __init__(self, nb_tiles_max=None, with_replacement=False, shuffle=True, target_label=None):
        super(RandomPerItemSampler, self).__init__(
            nb_tiles_max=nb_tiles_max, with_replacement=with_replacement, shuffle=shuffle)
        self.target_label = target_label

    def sample_tiles_from_candidates(self, candidate_tiles):
        sampled_tiles = []
        item_keys = list_utils.get_items_in_list(candidate_tiles)

        for item_key in item_keys:
            candidate_tiles_ = list_utils.filter_tiles_by_item(candidate_tiles, item_key)
            if self.target_label is not None:
                candidate_tiles_ = list_utils.filter_tiles_by_label(candidate_tiles_, self.target_label)

            nb_tiles_max = int((self.nb_tiles_max or len(candidate_tiles_)) / len(item_keys))

            sampled_tiles.extend(self._sample_n_tiles_from_list(candidate_tiles_, nb_tiles_max))

        return sampled_tiles


class StratifiedSampler(TilesSampler):
    """
    Samples randomly at most `nb_tiles_max` tiles from the candidates pool
    Tries to balance labels (globally) to the limit of the number of available tiles / label
    If with_replacement, ensure that a balanced sample is exactly attained
    """

    def __init__(self, nb_tiles_max=None, with_replacement=False, shuffle=True):
        super(StratifiedSampler, self).__init__(with_replacement=with_replacement, shuffle=shuffle)
        self.nb_tiles_max = nb_tiles_max

    def sample_tiles_from_candidates(self, candidate_tiles):
        sampled_tiles = []
        labels = list_utils.get_labels_in_list(candidate_tiles)

        for label in labels:
            candidate_tiles_ = list_utils.filter_tiles_by_label(candidate_tiles, label)

            nb_tiles_max = int((self.nb_tiles_max or len(candidate_tiles_)) / len(labels))

            sampled_tiles.extend(self._sample_n_tiles_from_list(candidate_tiles_, nb_tiles_max))

        return sampled_tiles


class StratifiedPerItemSampler(StratifiedSampler):
    """
    Samples randomly at most `nb_tiles_max` tiles from the candidates pool
    Tries to balance labels (globally) to the limit of the number of available tiles / label / item
    If with_replacement, ensure that a balanced sample is exactly attained
    """

    def __init__(self, nb_tiles_max=None, with_replacement=False, shuffle=True):
        super(StratifiedPerItemSampler, self).__init__(
            nb_tiles_max=nb_tiles_max, with_replacement=with_replacement, shuffle=shuffle)

    def sample_tiles_from_candidates(self, candidate_tiles):
        sampled_tiles = []
        labels = list_utils.get_labels_in_list(candidate_tiles)
        items = list_utils.get_items_in_list(candidate_tiles)

        for label in labels:
            for item in items:
                candidate_tiles_ = list_utils.filter_tiles_by_item_by_label(candidate_tiles, item, label)
                nb_tiles_max = int((self.nb_tiles_max or len(candidate_tiles_)) / (len(labels) * len(items)))
                sampled_tiles.extend(self._sample_n_tiles_from_list(candidate_tiles_, nb_tiles_max))

        return sampled_tiles


class BackgroundToPositiveRatioSampler(TilesSampler):
    """
    Samples randomly `nb_positive_tiles_max` in non background classes, - while balancing items
    Then samples `background_to_positive_ratio` * `nb_positive_tiles_max` in background tiles
    """

    def __init__(self, background_to_positive_ratio=1, nb_positive_tiles_max=None, with_replacement=False,
                 shuffle=True):
        super(BackgroundToPositiveRatioSampler, self).__init__(with_replacement=with_replacement, shuffle=shuffle)
        self.background_to_positive_ratio = background_to_positive_ratio
        self.nb_positive_tiles_max = nb_positive_tiles_max

    def sample_tiles_from_candidates(self, candidate_tiles):
        non_background_classes = list_utils.get_labels_in_list(candidate_tiles).remove("background")

        sampled_tiles = []

        for label in non_background_classes:
            candidate_tiles_ = list_utils.filter_tiles_by_label(candidate_tiles, label)

            nb_tiles_max = len(candidate_tiles_)
            if self.nb_positive_tiles_max is not None:
                nb_tiles_max = int(self.nb_positive_tiles_max / len(non_background_classes))

            sampled_tiles.extend(self._sample_n_tiles_from_list(candidate_tiles_, nb_tiles_max))

        # Sample tiles
        candidate_tiles_ = list_utils.filter_tiles_by_label(candidate_tiles, "background")
        nb_bg_tiles = self.background_to_positive_ratio * (self.nb_positive_tiles_max or len(sampled_tiles))
        sampled_tiles.extend(self._sample_n_tiles_from_list(candidate_tiles_, nb_bg_tiles))

        return sampled_tiles


class BackgroundToPositiveRatioPerItemSampler(BackgroundToPositiveRatioSampler):
    """
    Samples randomly `nb_positive_tiles_max` in non background classes, - while balancing items
    Then samples `background_to_positive_ratio` * `nb_positive_tiles_max` in background tiles
    Do it per item
    """

    def __init__(self, background_to_positive_ratio=1, nb_positive_tiles_max=None, with_replacement=False,
                 shuffle=True):
        super(BackgroundToPositiveRatioPerItemSampler, self).__init__(
            background_to_positive_ratio=background_to_positive_ratio,
            nb_positive_tiles_max=nb_positive_tiles_max,
            with_replacement=with_replacement,
            shuffle=shuffle)

    def sample_tiles_from_candidates(self, candidate_tiles):
        sampled_tiles = []
        items = list_utils.get_items_in_list(candidate_tiles)

        for item in items:
            candidate_tiles_ = list_utils.filter_tiles_by_item(candidate_tiles, item)
            non_background_classes = list_utils.get_labels_in_list(candidate_tiles_)
            non_background_classes.remove("background")

            nb_non_background_tiles = 0

            for label in non_background_classes:
                candidate_tiles__ = list_utils.filter_tiles_by_label(candidate_tiles_, label)

                nb_tiles_max = len(candidate_tiles__)
                if self.nb_positive_tiles_max is not None:
                    nb_tiles_max = int(self.nb_positive_tiles_max / (len(non_background_classes) * len(items)))

                sampled_tiles_ = self._sample_n_tiles_from_list(candidate_tiles__, nb_tiles_max)
                nb_non_background_tiles += len(sampled_tiles_)
                sampled_tiles.extend(sampled_tiles_)

            # Sample tiles
            candidate_tiles__ = list_utils.filter_tiles_by_label(candidate_tiles_, "background")
            nb_bg_tiles = self.background_to_positive_ratio * nb_non_background_tiles
            sampled_tiles.extend(self._sample_n_tiles_from_list(candidate_tiles__, nb_bg_tiles))

        return sampled_tiles
