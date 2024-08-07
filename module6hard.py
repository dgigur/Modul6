from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled=False):
        if isinstance(sides, int):
            sides = [sides]
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        if len(color) == 3:
            for i in color:
                if i in range(0, 256):
                    continue
                else:
                    print("Цвет выбран некорректно")
                    return False
            print('Цвет выбран корректно')
            return True
        else:
            print('Некорректный цвет')
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color((r, g, b)):
            self.__color = (r, g, b)
            return self.__color

    def __is_valid_sides(self, *args):
        counter = 0
        for i in args:
            counter += 1
            if i > 0 and isinstance(i, int):
                continue
            else:
                return False
        if counter == self.sides_count:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        list_of_sides = []
        if len(new_sides) == self.sides_count:
            for i in new_sides:
                list_of_sides.append(i)
            self.__sides = list_of_sides
            return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, sides, color):  #Зададим параметр длина окружности
        super().__init__(sides, color)
        self.__radius = self._Figure__sides[0] / (2 * pi)

    def get_square(self):
        S = pi * self.__radius ** 2
        return S


class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides, color):
        super().__init__(sides, color)
        p = sum(self._Figure__sides) / 2
        self.__height = 2 * sqrt(p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) *
                                 (p - self._Figure__sides[2])) / self._Figure__sides[0]
# Высота ищется 1 из 3. Остальные две ищутся аналогично.
    def get_square(self):
        S = self.__height * self._Figure__sides[0]


class Cube(Figure):
    sides_count = 12

    def __init__(self, sides, color):
        if isinstance(sides, int):
            sides = [sides] * 12
        super().__init__(sides, color)

    def get_volume(self):
        V = self._Figure__sides[0] ** 3
        return V


circle1 = Circle(10, (200, 200, 100))  # (Цвет, стороны)
cube1 = Cube(6, (222, 35, 130))


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())


# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка на треугольнике
triangle1 = Triangle([1, 2, 3], (200, 200, 100))
print(len(triangle1))
triangle1.set_color(111, 111, 123)
print(triangle1.get_color())
triangle1.set_sides(5, 3, 12)
print(triangle1.get_sides())
print(len(triangle1))
