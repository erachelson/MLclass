import json
import hashlib


class BoundingBox(object):
    """
    Base bounding box class. A Bounding Box is basically a rectangle with x_min, y_min width and height
    We follow numpy and opencv image conventions:
    (0,0) is top left, x is right and 2nd dim, y is bottom and 1st dim
    So an image is a matrix of shape (height, width, 3) where the three channels are r,g,b
    """

    def __init__(self, x_min, y_min, height, width):
        """

        Args:
            x_min:
            y_min:
            height:
            width:
        """
        self.height = int(height)
        self.width = int(width)
        self.x_min = int(x_min)
        self.y_min = int(y_min)

    @classmethod
    def from_bounds(cls, x_min, y_min, x_max, y_max):
        """
            Creates a BBox from x1,y1,x2,y2 instead of x1,y1,height,width
        Args:
            x_min:
            y_min:
            x_max:
            y_max:

        Returns:

        """
        return cls(x_min=x_min, y_min=y_min, width=x_max - x_min, height=y_max - y_min)

    @property
    def __geo_interface__(self):
        return {
            'type':
            'Polygon',
            'coordinates': [[(self.x_min, self.y_min), (self.x_max, self.y_min), (self.x_max, self.y_max),
                             (self.x_min, self.y_max)]]
        }

    @property
    def area(self):
        """

        Returns: the area of the bbox

        """
        return self.width * self.height

    @property
    def x_max(self):
        """

        Returns:

        """
        return self.x_min + self.width

    @property
    def y_max(self):
        """

        Returns:

        """
        return self.y_min + self.height

    @property
    def center(self):
        """

        Returns: (x,y) the center (float) of the bbox

        """
        return (self.x_min + self.x_max) / 2., (self.y_min + self.y_max) / 2.

    def contains_point(self, point, strict=False):
        """

        Args:
            point(tuple): (x,y)
            strict: strict inclusion or not

        Returns:

        """
        x, y = point
        if strict:
            return self.x_min < x < self.x_max and self.y_min < y < self.y_max
        else:
            return self.x_min <= x <= self.x_max and self.y_min <= y <= self.y_max

    def contains(self, bbox):
        """

        Args:
            bbox(BoundingBox):

        Returns: bool

        """
        return bbox.x_min >= self.x_min and \
               bbox.x_max <= self.x_max and \
               bbox.y_min >= self.x_min and \
               bbox.y_max <= self.y_max

    def intersects(self, bbox):
        """

        Args:
            bbox(BoundingBox):

        Returns: bool

        """
        x_min = max(self.x_min, bbox.x_min)
        y_min = max(self.y_min, bbox.y_min)
        x_max = min(self.x_max, bbox.x_max)
        y_max = min(self.y_max, bbox.y_max)

        return x_min < x_max and y_min < y_max

    def intersection(self, bbox):
        """

        Args:
            bbox(BoundingBox):

        Returns:
            BoundingBox if intersection else BoundingBox with height=0 and width=0
        """
        if self.intersects(bbox):
            x_min = max(self.x_min, bbox.x_min)
            y_min = max(self.y_min, bbox.y_min)
            x_max = min(self.x_max, bbox.x_max)
            y_max = min(self.y_max, bbox.y_max)
            return BoundingBox.from_bounds(x_min, y_min, x_max, y_max)
        else:
            return BoundingBox(x_min=self.x_min, y_min=self.y_min, height=0, width=0)

    def iou(self, bbox):
        """

        Args:
            bbox:

        Returns:
            intersection over union

        """
        if not self.intersects(bbox):
            return 0.
        else:
            x_min = max(self.x_min, bbox.x_min)
            y_min = max(self.y_min, bbox.y_min)
            x_max = min(self.x_max, bbox.x_max)
            y_max = min(self.y_max, bbox.y_max)
            return (x_max - x_min) * (y_max - y_min) / (self.area + bbox.area - (x_max - x_min) * (y_max - y_min))

    def translate(self, x_off, y_off):
        """

        Args:
            x_off:
            y_off:

        Returns:

        """
        self.x_min = self.x_min + x_off
        self.y_min = self.y_min + y_off

    def __repr__(self):
        """

        Returns:

        """
        return json.dumps(self.__dict__, indent=4)

    def __str__(self):
        """

        Returns:

        """
        s = ""
        s += "--- {} ---\n".format(self.__class__.__name__)
        for key, val in self.__dict__.items():
            s += "{}: {}\n".format(key, val)
        return s

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(tuple(sorted(tuple(self.__dict__.items()), key=lambda t: t[0])))

    @property
    def key(self):
        return hashlib.sha224(str(self.__hash__()).encode('utf-8')).hexdigest()
