from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """В данном контексте super().__init__()используется для вызова __init__ метода класса Turtle,
     Player от которого он наследуется. Это необходимо для обеспечения Turtle
    правильной инициализации объекта перед добавлением или изменением любых дополнительных свойств объекта Player."""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)          # на такой шаг всю дорогу двигаться