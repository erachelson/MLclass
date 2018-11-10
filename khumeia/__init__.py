import os

from khumeia.utils.logger import LOGGER
from khumeia.utils.get_data import download_train_data, download_eval_data

try:
    from joblib import Memory
    if os.environ.get("TP_ISAE_DATA") is not None:
        cache_dir = os.path.join(os.environ.get("TP_ISAE_DATA"), "cache")
    else:
        cache_dir = "/tmp/cache"

    memory = Memory(cache_dir, verbose=0)
except ImportError:
    memory = None
