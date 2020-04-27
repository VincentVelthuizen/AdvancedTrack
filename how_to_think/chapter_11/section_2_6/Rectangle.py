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

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, delta_x, delta_y):
        """ Move this object by the deltas """
        self.corner.x += delta_x
        self.corner.y += delta_y

    def area(self):
        """ Return the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """  Return the perimeter of the rectangle """
        return 2 * (self.width + self.height)

    def flip(self):
        """ Flip the height and width of the rectangle """
        # This is a trick to spare a "helper variable" we covered it in the basic track
        self.width, self.height = self.height, self.width

    def contains(self, point):
        """ Is point contained within this rectangle? """
        # Technically there are 4 comparisons here. Python struggles with the "newline" after the "and" so it needs to
        # be "escaped" (the backslash)
        # See the alternative version below if this version hurts your brain
        return (self.corner.x <= point.x < (self.corner.x + self.width)) and \
               (self.corner.y <= point.y < (self.corner.y + self.height))

    def contains_alternative(self, point):
        inside = True       # assume the point is inside the rectangle and look for proof of the contrary

        if self.corner.x > point.x:     # the top left corner is to the right of the point it must be outside the rect
            inside = False
        if point.x >= (self.corner.x + self.width):
            inside = False
        if self.corner.y > point.y:
            inside = False
        if point.y >= (self.corner.y + self.height):
            inside = False

        return inside

    def get_corners(self):
        top_left = self.corner
        top_right = Point(self.corner.x + self.width, self.corner.y)
        bottom_left = Point(self.corner.x, self.corner.y + self.height)
        bottom_right = Point(self.corner.x + self.width, self.corner.y + self.height)
        return [top_left, top_right, bottom_left, bottom_right]

    def collide(self, other_rectangle):
        colliding = False
        for corner in self.get_corners():
            if other_rectangle.contains(corner):
                colliding = True
        for corner in other_rectangle.get_corners():
            if self.contains(corner):
                colliding = True
        return colliding


if __name__ == "__main__":
    # this only gets executed when the file is run directly, not when it is included in another
    box = Rectangle(Point(0, 0), 100, 200)
    bomb = Rectangle(Point(100, 80), 5, 10)

    print("box ", box)
    print("bomb ", bomb)

    box.grow(50, -50)
    print("box ", box)

    box.move(100, 80)
    print("box ", box)
