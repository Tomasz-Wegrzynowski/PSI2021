


class Calculator:
    
    def dodaj(x,y):
        wynik = x+y
        return wynik
    def odejmij(x,y):
        wynik = x-y
        return wynik
    def pomnoz(x,y):
        wynik = x*y
        return wynik
    def podziel(x,y):
        wynik = x/y
        return wynik

class ScienceCalculator(Calculator):
    
    def potega(x):
        wynik = x**x
        return wynik

print(ScienceCalculator.potega(3))


