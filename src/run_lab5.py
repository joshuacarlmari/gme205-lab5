import json
from spatial import Parcel, Building, Road


with open("data/spatial_features.json") as f:
    data = json.load(f)

features = []

for item in data:

    geom = item["geometry"]
    ftype = item["type"]

    if ftype == "Parcel":
        features.append(Parcel(geom))

    elif ftype == "Building":
        floors = item["floors"]
        features.append(Building(geom, floors))

    elif ftype == "Road":
        width = item["width"]
        features.append(Road(geom, width))


if not features:
    print("Error: No spatial objects loaded")

else:

    total_area = 0
    area_by_type = {}

    for f in features:

        area = f.effective_area()
        total_area += area

        name = type(f).__name__

        if name not in area_by_type:
            area_by_type[name] = 0

        area_by_type[name] += area


    #print("Total Effective Area:", total_area)

    #print("\nArea by Feature Type")

    print("\nIndividual Feature Areas")

    for f in features:
        print(type(f).__name__, int(f.effective_area()))


    print("\nTotal Area by Feature Type")
    for key, value in area_by_type.items():
        print(f"{key}: {value:,.2f} m²")


    print(f"\nTotal Effective Area: {total_area:,.2f} m²")

