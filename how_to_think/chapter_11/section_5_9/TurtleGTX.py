from turtle import Turtle, Screen


class TurtleGTX(Turtle):

    def __init__(self):
        super().__init__()
        self.odometer = 0

    def forward(self, distance):
        super().forward(distance)
        self.odometer += abs(distance)

    def get_odo(self):
        return self.odometer


if __name__ == "__main__":
    screen = Screen()
    gtx = TurtleGTX()

    gtx.forward(-50)

    print(gtx.get_odo())

    screen.exitonclick()
