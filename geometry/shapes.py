import math
class Shape():
    def __init__(self, center_x: float = 0.0, center_y: float = 0.0):
        self.center_x = center_x
        self.center_y = center_y
        self.coordinates = []

    def translate(self, x: float, y: float):
        self.center_x += x
        self.center_y += y


class Triangle(Shape):
    def __init__(self, width: float, height: float, center_x: float = 0.0, center_y: float = 0.0):
        super().__init__(center_x, center_y)

        self.width = self.width
        self.height = self.height
        self.center_x = center_x
        self.center_y = center_y

    def area(self):
        return 0.5 * (self.width * self.height)



class RightTriangle(Triangle):
    def __init__(self, width, height, center_x = 0, center_y = 0):
        super().__init__(width, height, center_x, center_y)

        self.a = height
        self.b = width
        self.hyp = math.sqrt((self.a ** 2) + (self.b ** 2))
    
    def get_coordinates(self):

        width_radius = self.width / 2
        height_radius = self.height / 2

        vertex_0 = (self.center_x, self.center_y + height_radius)
        vertex_1 = (self.center_x - width_radius, self.center_y - height_radius)
        vertex_2 = (self.center_x + width_radius, self.center_y - height_radius)

        self.coordinates = [vertex_0, vertex_1, vertex_2]

        return self.coordinates


class Rectangle(Shape):
    def __init__(self, height: float, width: float, center_x: float= 0.0, center_y: float = 0.0):
        super().__init__(center_x, center_y)

        self.height = height
        self.width = width
        self.center_x = center_x
        self.center_y = center_y
        self.coordinates = []

    def area(self):
        return self.width * self.height


    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def get_coordinates(self) -> list[tuple]:
        if self.coordinates:
            return self.coordinates
        
        width_radius = self.width / 2
        height_radius = self.height / 2

        vertex_0 = (width_radius + self.center_x, height_radius + self.center_y)
        vertex_1 = (self.center_x - width_radius, height_radius + self.center_x)
        vertex_2 = (self.center_x - width_radius, self.center_y - height_radius)
        vertex_3 = (width_radius + self.center_x, self.center_y - height_radius)

        self.coordinates = [vertex_0, vertex_1, vertex_2, vertex_3]
        return self.coordinates



class Square(Rectangle):
    def __init__(self, side_length: float, center_x: float = 0, center_y: float = 0.0):
        super().__init__(side_length, side_length, center_x, center_y)


class Circle(Shape):
    def __init__(self, radius: float = 1.0,center_x = 0.0, center_y = 0.0):
        super().__init__(center_x, center_y)
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * (self.radius **2)
    
    def circumference(self) -> float:
        return 2 * math.pi * self.radius
    