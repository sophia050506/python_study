class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return  "(%g, %g)" % (self.x, self.y)

    def print_point(self):
        print("(%g, %g)" % (self.x, self.y))

    def __add__(self, other):
        if isinstance(other, Point):
            self.x += other.x
            self.y += other.y
            return self
        elif isinstance(other, tuple):
            self.x += other[0]
            self.y += other[1]
            return self


p = Point(3)
#p.print_point()
print(p)
p1 = Point(2,3)
print(p + p1)
p2 = (1,2)
print(p + p2)
vars(p)