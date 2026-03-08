from shapely.geometry import shape

class SpatialObject:
    def effective_area(self):
        """"
        Return the spatial area representation of the object.
        Subclasses must implement this behavior
        """
        raise NotImplementedError

class Parcel(SpatialObject):
    def effective_area(self):
        return self.geometry.area
    
class Building(SpatialObject):
    def effective_area(self):
        return self.geometry.area * self.floors
    
class Road(SpatialObject):
    def effective_area(self):
        return self.geometry.buffer(self.width).area

