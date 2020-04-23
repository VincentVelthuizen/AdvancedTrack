from how_to_think.chapter_11.section_1_12.Point import Point


def distance(p1, p2):
    delta_x = p1.x - p2.x
    delta_y = p1.y - p2.y
    return ((delta_x ** 2) + (delta_y ** 2)) ** 0.5


point_a = Point(1, 1)
point_b = Point(4, 5)
print(distance(point_a, point_a))
print(distance(point_a, point_b))
