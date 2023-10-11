class Turtle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            print("Нельзя уменьшить s ниже 1")

    def count_moves(self, x2, y2):
        x_diff = abs(self.x - x2)
        y_diff = abs(self.y - y2)
        if x_diff % self.s == 0 and y_diff % self.s == 0:
            return (x_diff + y_diff) // self.s
        else:
            return "Невозможно достичь указанной точки с текущим размером шага"

turtle = Turtle(0, 0, 2)

turtle.go_up()
turtle.go_right()
turtle.evolve()
turtle.go_down()
turtle.go_left()
print(turtle.x, turtle.y, turtle.s)

turtle.degrade()
print(turtle.s)

print(f"Текущая позиция: {turtle.x, turtle.y}")
x2 = 3
y2 = 4
moves = turtle.count_moves(x2, y2)
print(moves)

turtle.degrade()
turtle.go_up()
turtle.go_right()
turtle.evolve()
print(f"Текущая позиция: {turtle.x, turtle.y}")
print(turtle.count_moves(3, 4))
print(turtle.count_moves(4, 4))
