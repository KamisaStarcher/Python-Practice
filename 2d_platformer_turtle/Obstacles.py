import turtle
import Settings

class Obstacle(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.penup()
        self.color = "red"
        self.shape = "sqaure"
        self.x = x
        self.y = y
        self.dx = -0.5

    def move(self):
        if (self.x-self.dx) < -Settings.SCREEN_WIDTH:
            self.x = Settings.SCREEN_WIDTH

        else:
            self.x += self.dx

    def show(self):
        self.setx(self.x)
        self.sety(self.y)

    def update(self):
        self.show()
        self.move()