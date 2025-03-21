class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def evaluate(self, x):
        return self.a * x ** 2 + self.b * x + self.c

a = float(input("Enter the value for a: "))
b = float(input("Enter the value for b: "))
c = float(input("Enter the value for c: "))
x = float(input("Enter the value for x: "))

quadratic = QuadraticEquation(a, b, c)
print("The computed value of y is:", quadratic.evaluate(x))
