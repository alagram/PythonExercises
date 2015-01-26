class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y


point1 = Point(8, 5)
point2 = Point(-6, 1)


print(point1 + point2)
print(point1 - point2)
print(point1)
print(point2)