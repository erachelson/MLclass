from khumeia.roi.tile import Tile, LabelledTile


def filter_tiles_by_item(tiles_list, item_key):
    """
    Operation on list of Tiles
    Args:
        tiles_list(list[Tile]):
        item_key:

    Returns:

    """
    if hasattr(item_key, "key"):
        item_key = item_key.key
    else:
        item_key = item_key
    return list(filter(lambda tile: tile.item_id == item_key, tiles_list))


def filter_tiles_by_label(tiles_list, label):
    """
    Operation on list of Tiles: Filter tiles list by tile.label

    Args:
        tiles_list(list[LabelledTile]):
        label:

    Returns:

    """
    return list(filter(lambda tile: tile.label == label, tiles_list))


def filter_tiles_by_item_by_label(tiles_list, item_key, label):
    """
        Operation on list of Tiles: Filter tiles by tile.item_id and tile.label

    Args:
        tiles_list(list[LabelledTile]):
        item_key:
        label:

    Returns:

    """
    return filter_tiles_by_label(filter_tiles_by_item(tiles_list, item_key), label)


def flatten_list(tiles_list):
    """
        From a list(list(Tiles)) get a list(Tiles))
        [item for sublist in tiles_list for item in sublist]
    Args:
        tiles_list:

    Returns:

    """
    return [item for sublist in tiles_list for item in sublist]


def get_labels_in_list(tiles_list):
    """
        list(set([tile.label for tile in tiles_list]))
    Args:
        tiles_list:

    Returns:

    """
    return list(set([tile.label for tile in tiles_list]))


def get_items_in_list(tiles_list):
    """
        list(set([tile.item_id for tile in tiles_list]))
    Args:
        tiles_list:

    Returns:

    """
    return list(set([tile.item_id for tile in tiles_list]))
