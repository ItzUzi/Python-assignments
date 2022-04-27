class Pair:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "<%d, %d>" % (self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Pair(x, y)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Pair(x, y)

    def __truediv__(self, other):
        x = self.x * self.y - other.x * other.y
        y = self.x * other.x - self.y * other.y
        return Pair(x, y)


def main():
    p1 = Pair(3, 2)
    p2 = Pair(1, 5)
    p3 = Pair(4, 3)

    print("p1:", p1)
    print("p2:", p2)
    print("p3:", p3)

    print(p1 + p2)
    print(p1 * p2)
    print(p1 / p2)
    print(p1 + p2 * p3)
    print(p1 * p2 / p3 + p1)


if __name__ == '__main__':
    main()
