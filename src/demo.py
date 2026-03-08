from shapely.geometry import Polygon, LineString
from spatial import Parcel, Building, Road


parcel = Parcel({
    "type": "Polygon",
    "coordinates": [[[0,0],[0,10],[10,9],[10,0],[0,0]]]
})

building = Building({
    "type": "Polygon",
    "coordinates": [[[0,0],[0,5],[4,5],[5,0],[0,0]]]
}, floors=3)

road = Road({
    "type": "LineString",
    "coordinates": [[0,0],[19,0]]
}, width=2)


features = [parcel, building, road]

for f in features:
    print(type(f).__name__, f.effective_area())