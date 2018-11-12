import cv2
from khumeia.utils import list_utils
from khumeia.roi.tile import BoundingBox, LabelledTile, Tile, PredictionTile


def draw_bbox_on_image(image, bbox, color=(0, 255, 0), thickness=2):
    """
    Draw one BoundingBox to an image using cv2.rectangle
    Args:
        image(np.ndarray): A (h,w,3) 8-bit array representing the image
        bbox(BoundingBox):
        color: A tuple (r,g,b) [0,255]
        thickness(int): A thickness value

    Returns:
        The same `image` but with the bounding box drawn on it

    """
    cv2.rectangle(image, (bbox.x_min, bbox.y_min), (bbox.x_max, bbox.y_max), color=color, thickness=thickness)
    return image


def draw_bboxes_on_image(image, bboxes, color=(0, 255, 0), thickness=2):
    """
    Draw BoundingBoxes to an image using cv2.rectangle
    Args:
        image:
        bboxes:
        color:
        thickness:

    Returns:

    """
    len(bboxes)
    for bbox in bboxes:
        image = draw_bbox_on_image(image, bbox, color=color, thickness=thickness)
    return image


def draw_item(item):
    """
        Draw an item labels on its image
    Args:
        item:

    Returns:

    """
    image = item.image
    labels = item.labels
    image = draw_bboxes_on_image(image, labels, color=(0, 255, 0))
    return image


def draw_item_with_tiles(item, tiles=None):
    """
        Draw an item labels on its images as well as the tiles in tiles
    Args:
        item:
        tiles(list[LabelledTIles]):

    Returns:

    """
    image = draw_item(item)
    if tiles is not None:
        tiles = list_utils.filter_tiles_by_item(tiles, item.key)
        tiles_bg = list_utils.filter_tiles_by_label(tiles, "background")
        image = draw_bboxes_on_image(image, tiles_bg, color=(255, 0, 0))
        tiles_ac = list_utils.filter_tiles_by_label(tiles, "aircraft")
        image = draw_bboxes_on_image(image, tiles_ac, color=(0, 0, 255))

    return image


def draw_item_with_results(item, results=None):
    """
        Draw an item labels on its images as well as the PredictionTiles in Tiles
    Args:
        item:
        results(list[PredictionTile]):

    Returns:

    """
    image = draw_item(item)
    if results is not None:
        tiles = list(filter(lambda tile: tile.item_id == item.key, results))
        true_positives = list(filter(lambda tile: tile.is_true_positive, tiles))
        false_positives = list(filter(lambda tile: tile.is_false_positive, tiles))
        false_negatives = list(filter(lambda tile: tile.is_false_negative, tiles))
        image = draw_bboxes_on_image(image, true_positives, color=(0, 255, 0))
        image = draw_bboxes_on_image(image, false_positives, color=(0, 0, 255))
        image = draw_bboxes_on_image(image, false_negatives, color=(255, 0, 0))

    return image
