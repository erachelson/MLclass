import geojson
from khumeia.roi.bounding_box import BoundingBox


def test_bbox():
    box = BoundingBox(x_min=0, y_min=0, width=256, height=256)

    assert box.area == 256 * 256
    assert box.x_max == 256
    assert box.y_max == 256

    assert isinstance(box.__dict__, dict)
    print(box)


def test_bbox_int():
    box1 = BoundingBox(4, 4, 16, 16)
    box2 = BoundingBox(2, 2, 1, 1)
    box3 = BoundingBox(7, 7, 4, 4, )
    assert not box1.intersects(box2)
    assert box1.intersects(box3)

    assert box1.intersection(box2).area == 0.
    assert box1.intersection(box3).area > 0.


def test_bbox_iou():
    box1 = BoundingBox(4, 4, 16, 16)
    box2 = BoundingBox(4, 4, 16, 16)
    box3 = BoundingBox(4, 4, 2, 2)
    box4 = BoundingBox(7, 7, 4, 4)

    assert box1.iou(box2) == 1.0
    assert box1.iou(box3) == 2 * 2 / (16 * 16)
    assert box1.iou(box4) == 4 * 4 / (16 * 16 + 4 * 4 - 4 * 4)
    assert box3.iou(box4) == 0.


def test_geojson():
    try:
        import shapely.geometry
        box1 = BoundingBox(4, 4, 16, 16)
        assert geojson.FeatureCollection(features=[box1])
        print(shapely.geometry.shape(box1))
        print(shapely.geometry.box(4, 4, 20, 20))
        assert shapely.geometry.shape(box1).equals(shapely.geometry.box(4, 4, 20, 20))
    except ImportError:
        pass
