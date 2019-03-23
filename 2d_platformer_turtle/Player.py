import turtle
class Player(turtle.Turtle):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.penup()
        self.x = x
        self.y = y
        self.jump_time = 20

    def Jump(self):
        for i in range(20):
            dy = i
            if i < self.jump_time:
                dy *= -1
            
            self.y += (dy)
            self.show()

    def show(self):
        self.setx(self.x)
        self.sety(self.y)

    def update(self):
        self.show()