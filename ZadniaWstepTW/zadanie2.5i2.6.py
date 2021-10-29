class Calculator:

    def add(a, b):
        return a+b

    def difference(a, b):
        return a-b

    def multiply(a, b):
        return a*b

    def divide(a, b):
        if b == 0:
            return "Nie można dzielić przez 0"
        else:
            return a/b

class ScienceCalculator(Calculator):

    def exponentiation(a, b):
        c = a
        if(b==0):
            return 1
        c = a**b
        return c


print(Calculator.add(3, 5))
print(Calculator.difference(3, 5))
print(Calculator.multiply(3, 5))
print(Calculator.divide(3, 5))
print(ScienceCalculator.exponentiation(-2, 2))
