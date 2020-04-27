from how_to_think.chapter_11.section_1_12.Point import Point
from how_to_think.chapter_11.section_2_6.Rectangle import Rectangle
from how_to_think.test.test import test

player = Rectangle(Point(0, 0), 5, 10)
obstacle = Rectangle(Point(20, 0), 20, 20)

test(not player.collide(obstacle))
player.move(20, 0)
test(player.collide(obstacle))

"""
types of collision:

corners overlapping (each has a corner in the other)
sides overlapping (one has two corners in the other)
fully overlapping (one has four corners in the other)

if any corner is inside the other rectangle there is a collision,
checking all corners of one and opposite corners (e.g. top left en bottom right)
for simplification in the code I checked all corners for both rectangles
if none are in the other there is certainly no collision
"""