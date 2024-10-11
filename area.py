import math


class Shape:
    __rect = 0
    __circ = 0

    def area(self, *args):
        try:
            for el in args:
                if type(el) != int and type(el) != float:
                    raise Exception('Error: Values must be int or float..')

            if 0 < len(args) < 2:
                print('\n1 value received\nSet as "Diameter"')
                self.__circ = args[0] ** 2 / math.pi * 4
                return self.__circ
            elif 0 < len(args) < 3:
                print('\n2 values received\nSet as "axis:x, axis:y"')
                self.__rect = math.prod(list(args))
                return self.__rect
            else:
                print('\nError: Numbers of Values is Out of Range')
                return None
        except (TypeError, ValueError):
            print('Error: Values must be int or float..')


class Rectangle(Shape):
    # pass
    def area(self, x=0, y=0):
        if type(x) == int or type(x) == float:
            if type(y) == int or type(y) == float:
                print('\nRectangle:')
                return x * y
        raise Exception('Error: Values must be int or float..')


class Circle(Shape):
    def area(self, value=0):
        if type(value) == int or type(value) == float:
            print('\nCircle:')
            return value ** 2 / math.pi * 4  # S = D^2 / 4Pi
        raise Exception('Error: Values must be int or float..')


if __name__ == '__main__':
    shape = Shape()
    s_rect = Rectangle()
    s_circ = Circle()

    _rect = s_rect.area(3, 4)
    print(f'The Area of Shape: {_rect}')
    print('_' * 60)

    _circ = s_circ.area(10)  # По Диаметру
    print(f'The Area of Shape: {_circ}')
    print('_' * 60)

    s_main = shape.area(2, 5)  # Круг или Прямоугольник
    print(f'\nThe Area of Shape: {s_main}')
