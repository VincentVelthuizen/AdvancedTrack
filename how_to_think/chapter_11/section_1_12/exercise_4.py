from how_to_think.chapter_11.section_1_12.Point import Point

print(Point(4, 11).get_line_to(Point(6, 15)))

# The following line goes straight up/down, has no y_intercept and thus breaks the code
print(Point(4, 11).get_line_to(Point(4, 15)))
