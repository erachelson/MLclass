import json
import skimage.io
import warnings
from khumeia import memory
from khumeia.roi.groundtruth import Groundtruth


def _read_json(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)


if memory is not None:
    imread = memory.cache(skimage.io.imread)
    read_json = memory.cache(_read_json)
else:
    imread = skimage.io.imread
    read_json = _read_json


def read_aircraft_labels(labels_file):
    labels_data = read_json(labels_file)
    labels = []
    for label in labels_data['markers']:
        x, y, w = label['x'], label['y'], label['w']
        labels.append(Groundtruth(x_min=x, y_min=y, width=w, height=w, label="aircraft"))

    return labels


def imsave(fname, arr):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        skimage.io.imsave(fname, arr)
