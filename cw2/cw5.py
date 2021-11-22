



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

print(Calculator.dodaj(5,10))
print(Calculator.odejmij(5,10))
print(Calculator.pomnoz(5,10))
print(Calculator.podziel(5,10))