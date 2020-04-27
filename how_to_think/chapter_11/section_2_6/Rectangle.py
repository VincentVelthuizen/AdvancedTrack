from how_to_think.chapter_11.section_1_12.Point import Point


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "{0}, {1}, {2}".format(self.corner, self.width, self.height)


if __name__ == "__main__":
    # this only gets executed when the file is run directly, not when it is included in another
    box = Rectangle(Point(0, 0), 100, 200)
    bomb = Rectangle(Point(100, 80), 5, 10)

    print("box ", box)
    print("bomb ", bomb)
