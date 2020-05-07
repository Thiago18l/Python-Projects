import datetime

today = datetime.datetime.now()

print(str(today))
print(repr(today))

# When writing a class, you can override these methods to do whatever you want:

class Represent(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
        def __repr__(self):
            return "Represent (x={}, y=\"{}\")".format(self.x, self.y)
        def __str__(self):
            return "Representing x as {} and y as {}".format(self.x, self.y)


r = Represent(1, "Hopper")
print(r)
print(r.__repr__)
rep = r.__repr__()
print(rep)
