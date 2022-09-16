from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    # getting the turtle to move from whatever the ycor is + the move distance stated
    def movement(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    # telling the turtle to go to start after it reaches the finish line
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    # saying if ycor is greater than Finish_line_y(280) then it will return true else it's false
    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False





