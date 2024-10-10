import math


class Shape:
    def area(self, *args):
        raise NotImplementedError('\nOut of Subclass method')


class Rectangle(Shape):
    def area(self, x=0, y=0):
        if x != y:
            return x * y
        else:
            print(f'\nNOT a RECTANGLE !\nSquare Area: {x * y}')


class Circle(Shape):
    def area(self, l=0):
        return math.sqrt(l) / (math.pi * 4)


if __name__ == '__main__':
    shape = Shape()
    r_pr = Rectangle()
    c_pr = Circle()

    try:
        _rect = r_pr.area(4, 3)
        print(f'\nThe Area of RECTANGLE: {_rect}')

        _circ = c_pr.area(100)
        print(f'\nThe Area of CIRCLE: {_circ}')
    except Exception as ex:
        print(ex)

    # try:
    #     print(shape.area())
    # except Exception as e:
    #     print(e)
