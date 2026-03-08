import json
from spatial import Parcel

import json
from spatial import Parcel
import analysis


def load_parcels(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)