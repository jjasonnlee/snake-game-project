from turtle import Turtle
snake_position = [(0, 0), (-20, 0), (-40, 0)]
move_forward = 20
up = 90
down = 270
right = 0
left = 180

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in snake_position:
            self.add_body(position)

    def add_body(self, position):
        box = Turtle()
        box.penup()
        box.shape("square")
        box.color("white")
        box.setposition(position)
        self.snakes.append(box)

    def extend(self):
        self.add_body(self.snakes[-1].position())


    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[i - 1].xcor()
            new_y = self.snakes[i - 1].ycor()
            self.snakes[i].setposition(new_x, new_y)
        self.head.fd(move_forward)

    def up(self):
        if self.head.setheading != down:
            self.head.setheading(up)

    def down(self):
        if self.head.setheading != up:
            self.head.setheading(down)

    def left(self):
        if self.head.setheading != right:
            self.head.setheading(left)

    def right(self):
        if self.head.setheading != left:
            self.head.setheading(right)