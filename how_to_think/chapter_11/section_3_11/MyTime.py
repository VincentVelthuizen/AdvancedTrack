class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """
        Create a new MyTime object initialized to hrs, mins, secs.
        The values of mins and secs may be outside the range 0-59,
        but the resulting MyTime object will be normalized.
        """

        # Calculate total seconds to represent
        total_seconds = hrs*3600 + mins*60 + secs
        self.hours = total_seconds // 3600
        # Split in h, m, s
        left_over_seconds = total_seconds % 3600
        self.minutes = left_over_seconds // 60
        self.seconds = left_over_seconds % 60

    def __str__(self):
        return "{}:{}:{}".format(self.hours, self.minutes, self.seconds)

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        return MyTime(0, 0, self.to_seconds() - other.to_seconds())

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def increment(self, seconds):
        return MyTime(0, 0, self.to_seconds() + seconds)

    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self > time2

    def between(self, t1, t2):
        return t1 <= self < t2
