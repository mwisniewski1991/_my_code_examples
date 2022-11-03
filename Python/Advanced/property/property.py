# Main usage of @property
class Circle:
    def __init__(self, radius: float) -> None:
        self._radius = radius

    @property
    def radius(self):
        """The Radius property"""
        print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Set radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self._radius

circle = Circle(10.0)

print(circle.radius)
circle.radius = 15

print(circle.radius)

del circle.radius
print(circle.radius)


# Implemetning new attribute Diamater align with previous implementation.
class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius #In this case _radius changes to radius.

    @property
    def radius(self):
        """The Radius property"""
        # print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        # print("Set radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        # print("Delete radius")
        del self._radius

    @property
    def diamater(self):
        return self.radius * 2 #Diamater property under the hood read variable radius and multiply by 2

    @diamater.setter
    def diamater(self, value):
        self.radius = value / 2 #Diamater property under the hood save variable to Radius 
    
circle = Circle(10)
print(circle.radius)
print(circle.diamater)
print("CHANGE")
circle.radius = 8.5 #now change can be done with radius
print(circle.radius)
print(circle.diamater)
print("CHANGE")
circle.diamater = 80 # or with diamater
print(circle.radius)
print(circle.diamater)