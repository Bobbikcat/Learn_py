from math import pi
from abc import abstractmethod


class Shape:
    def __init__(self, size=0):
        self.size = size

    @abstractmethod
    def area(self, *args):
        return self.size


class Rectangle(Shape):
    def area(self, w=0, h=0):
        return w * h


class Circle(Shape):
    def area(self, r=0):
        return pi * r ** 2


if __name__ == '__main__':
    shape = Shape(size=666)
    print(f'Size of Shape: {shape.area()}')

    s_rect = Rectangle()
    _rectangle = s_rect.area(5, 5)
    print(f'Rectangle Area: {_rectangle}')

    s_circ = Circle()
    _circle = s_circ.area(10)
    print(f'Circle Area: {_circle}')
