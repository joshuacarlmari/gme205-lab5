from shapely.geometry import shape
from shapely.ops import transform
from pyproj import Transformer


transformer = Transformer.from_crs("epsg:4326", "epsg:32651", always_xy=True)

def project_geom(geom):
    return transform(transformer.transform, geom)


class SpatialObject:
    def __init__(self, geometry):
        self.geometry = shape(geometry)
        self.geometry = project_geom(self.geometry) 

    def effective_area(self):
        """
        Return the spatial area representation of the object in meters².
        Subclasses implement actual computation.
        """
        raise NotImplementedError


class Parcel(SpatialObject):
    def effective_area(self):
        return self.geometry.area 


class Building(SpatialObject):
    def __init__(self, geometry, floors):
        super().__init__(geometry)
        self.floors = floors

    def effective_area(self):
        return self.geometry.area * self.floors


class Road(SpatialObject):
    def __init__(self, geometry, width):
        super().__init__(geometry)
        self.width = width 

    def effective_area(self):
        return self.geometry.buffer(self.width).area