import json

from khumeia.roi.tile import LabelledTile


class SlidingWindow(object):
    """

    ![example1](https://cdn-images-1.medium.com/max/800/1*FHEOyHm1BTWyygQcgvNSXQ.png)

    Sample cutouts of a sliding window iterating from top to bottom (Imagery Courtesy of DigitalGlobe)

    ![example2](https://cdn-images-1.medium.com/max/800/1*BkQLxT_FVz6XqHul5qezEw.gif)

    Sliding window shown iterating across an image (left).
    An image classifier is applied to these cutouts and anything resembling a boat is saved as a positive (right)
    (Imagery Courtesy of DigitalGlobe)

    """

    def __init__(self,
                 tile_size=64,
                 padding=0,
                 stride=64,
                 discard_background=False,
                 label_assignment_mode="center",
                 intersection_over_area_threshold=0.5,
                 data_transform_fn=None):
        """

        Args:
            tile_size:
            padding:
            stride:
            discard_background:
            label_assignment_mode:
            intersection_over_area_threshold:
            data_transform_fn:
        """
        self.tile_size = tile_size
        self.stride = stride
        self.padding = padding
        self.label_assignment_mode = label_assignment_mode
        self.ioa_threshold = intersection_over_area_threshold
        self.discard_background = discard_background
        self.data_transform_fn = data_transform_fn

    def get_tiles_for_item(self, item):
        """

        Args:
            item:

        Returns:

        """
        labels = item.labels

        tiles = LabelledTile.get_tiles_for_item(
            item.key,
            item.shape,
            tile_shape=(self.tile_size, self.tile_size),
            padding=self.padding,
            stride=float(self.stride) / self.tile_size,
            data_transform_fn=self.data_transform_fn)

        tiles_with_labels = []

        for tile in tiles:
            assert isinstance(tile, LabelledTile)
            if self.label_assignment_mode == "center":
                tile.set_label_from_bboxes_center(labels)
            else:
                tile.set_label_from_bboxes_ioa(labels, ioa_threshold=self.ioa_threshold)

            if tile.label != "background" or not self.discard_background:
                tiles_with_labels.append(tile)

        return tiles_with_labels

    def __repr__(self):
        return json.dumps(self.__dict__, indent=4)

    def __str__(self):
        d = dict()
        d['class'] = self.__class__.__name__
        d.update(self.__dict__)
        return json.dumps(d, indent=4)
