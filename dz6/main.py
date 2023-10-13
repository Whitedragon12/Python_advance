class frange:
    def __init__(self, *args):
        if len(args) == 1:
            self.start = 0.0
            self.stop = args[0]
            self.step = 1.0
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1.0
        elif len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        else:
            raise TypeError("frange() accepts 1 to 3 arguments, but got %d" % len(args))

    def __iter__(self):
        current = self.start
        if self.step > 0:
            while current < self.stop:
                yield current
                current += self.step
        elif self.step < 0:
            while current > self.stop:
                yield current
                current += self.step


for i in frange(1, 100, 3.5):
    print(i)


# Перевірка зазначених тестів
assert(list(frange(5)) == [0, 1, 2, 3, 4])
assert(list(frange(2, 5)) == [2, 3, 4])
assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(frange(1, 5)) == [1, 2, 3, 4])
assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(frange(0, 0)) == [])
assert(list(frange(100, 0)) == [])

print('SUCCESS!')
