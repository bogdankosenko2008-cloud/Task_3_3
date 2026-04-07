import math
import turtle
class Figure:
    def dimention(self):
        raise NotImplementedError()
    def perimetr(self):
        return None
    def square(self):
        return None
    def squareSurface(self):
        return None
    def squareBase(self):
        return None
    def height(self):
        return None
    def volume(self):
        if self.dimention() == 2:
            return self.square()
        else:
            return None

#2D ФІГУРИ
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def dimention(self):
        return 2
    def perimetr(self):
        return self.a + self.b + self.c
    def square(self):
        p = self.perimetr() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b
    def dimention(self):
        return 2
    def perimetr(self):
        return 2 * (self.a + self.b)
    def square(self):
        return self.a * self.b

class Circle(Figure):
    def __init__(self, r):
        self.r = r
    def dimention(self):
        return 2
    def perimetr(self):
        return 2 * math.pi * self.r
    def square(self):
        return math.pi * self.r ** 2
class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d
    def dimention(self):
        return 2
    def perimetr(self):
        return self.a + self.b + self.c + self.d
    def square(self):
        p = self.perimetr() / 2
        return math.sqrt((p-self.a)*(p-self.b)*(p-self.c)*(p-self.d))

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h
    def dimention(self):
        return 2
    def perimetr(self):
        return 2 * (self.a + self.b)
    def square(self):
        return self.a * self.h

#3D ФІГУРИ

class Ball(Figure):
    def __init__(self, r):
        self.r = r
    def dimention(self):
        return 3
    def squareSurface(self):
        return 4 * math.pi * self.r**2
    def volume(self):
        return (4/3) * math.pi * self.r**3

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h
    def dimention(self):
        return 3
    def squareBase(self):
        return super().square()
    def volume(self):
        return (1/3) * self.squareBase() * self.h
    def height(self):
        return self.h


class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h
    def dimention(self):
        return 3
    def squareBase(self):
        return super().square()
    def volume(self):
        return (1/3) * self.squareBase() * self.h
    def height(self):
        return self.h

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
    def dimention(self):
        return 3
    def squareSurface(self):
        return 2 * (self.a*self.b + self.a*self.c + self.b*self.c)
    def volume(self):
        return self.a * self.b * self.c
    def height(self):
        return self.c

class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h
    def dimention(self):
        return 3
    def squareBase(self):
        return super().square()
    def volume(self):
        return (1/3) * math.pi * self.r**2 * self.h
    def height(self):
        return self.h


class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h
    def dimention(self):
        return 3
    def squareBase(self):
        return super().square()
    def volume(self):
        return self.squareBase() * self.h
    def height(self):
        return self.h

#СТВОРЕННЯ ФІГУР

def create_figure(line):
    parts = line.split()
    name = parts[0]
    nums = list(map(float, parts[1:]))

    if name == "Triangle":
        return Triangle(*nums)
    elif name == "Rectangle":
        return Rectangle(*nums)
    elif name == "Trapeze":
        return Trapeze(*nums)
    elif name == "Parallelogram":
        return Parallelogram(*nums)
    elif name == "Circle":
        return Circle(*nums)
    elif name == "Ball":
        return Ball(*nums)
    elif name == "TriangularPyramid":
        return TriangularPyramid(*nums)
    elif name == "QuadrangularPyramid":
        return QuadrangularPyramid(*nums)
    elif name == "RectangularParallelepiped":
        return RectangularParallelepiped(*nums)
    elif name == "Cone":
        return Cone(*nums)
    elif name == "TriangularPrism":
        return TriangularPrism(*nums)
    return None

def main():
    figures = []
    valid_figures = []
    try:
        with open("input01_02.txt", "r") as file:
            for line in file:
                if not line.strip():
                    continue

                try:
                    fig = create_figure(line.strip())
                    if fig:
                        figures.append(fig)
                except Exception as e:
                    print(f"Помилка створення фігури: {line.strip()} -> {e}")
        if not figures:
            print("Список фігур порожній")
            return
        for fig in figures:
            try:
                val = fig.volume()
                if val is not None and val >= 0:
                    valid_figures.append((fig, val))
            except Exception as e:
                print(f"Помилка обчислення: {type(fig).__name__} -> {e}")
        if not valid_figures:
            print("Немає коректних фігур")
            return
        max_figure, max_value = max(valid_figures, key=lambda x: x[1])
        print("Найбільша міра:", max_value)
        print("Тип фігури:", type(max_figure).__name__)
    except FileNotFoundError:
        print("Файл input01_02.txt не знайдено")
import turtle

# створення екрану
screen = turtle.Screen()
screen.title("UML Diagram")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


# 🔲 функція для малювання класу
def draw_class(x, y, text):
    t.penup()
    t.goto(x, y)
    t.pendown()

    width = 180
    height = 60

    # прямокутник
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

    # текст
    t.penup()
    t.goto(x + 10, y - 30)
    t.write(text, font=("Arial", 10, "normal"))


# ➡️ стрілка (наслідування)
def draw_arrow(x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)


# 🔷 Figure
draw_class(-90, 200, "Figure")

# 🔷 2D
draw_class(-300, 50, "Triangle")
draw_class(-100, 50, "Rectangle")
draw_class(100, 50, "Circle")
draw_class(-200, -100, "Trapeze")
draw_class(0, -100, "Parallelogram")

# 🔶 3D
draw_class(300, 50, "Ball")
draw_class(300, -100, "Cone")
draw_class(-300, -250, "TriangularPyramid")
draw_class(-100, -250, "QuadrangularPyramid")
draw_class(100, -250, "RectangularParallelepiped")
draw_class(300, -250, "TriangularPrism")

# 🔗 зв'язки

# до Figure
draw_arrow(-210, 50, -10, 200)   # Triangle
draw_arrow(-10, 50, -10, 200)    # Rectangle
draw_arrow(190, 50, -10, 200)    # Circle
draw_arrow(390, 50, -10, 200)    # Ball

# від Circle
draw_arrow(390, -100, 190, 50)   # Cone

# від Triangle
draw_arrow(-210, -250, -210, 50) # TriangularPyramid
draw_arrow(290, -250, -210, 50)  # TriangularPrism

# від Rectangle
draw_arrow(-10, -250, -10, 50)   # QuadrangularPyramid
draw_arrow(190, -250, -10, 50)   # RectangularParallelepiped

# додаткові
draw_arrow(-210, -100, -210, 50) # Trapeze
draw_arrow(10, -100, -10, 50)    # Parallelogram

turtle.done()
if __name__ == "__main__":
    main()
