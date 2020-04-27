from how_to_think.chapter_11.section_3_11.MyTime import MyTime
from how_to_think.test.test import test

start = MyTime(3, 0, 0)
end = MyTime(4, 0, 0)
now = MyTime(3,40,30)

test(now.between(start, end))
