from how_to_think.chapter_11.section_3_11.MyTime import MyTime
from how_to_think.test.test import test_equal

time = MyTime(3, 0, 0)

test_equal(time.increment(65), MyTime(3, 1, 5))
test_equal(time.increment(-65), MyTime(2, 58, 55))
