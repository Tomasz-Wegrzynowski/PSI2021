def temperature_changer(temperature_type, degrees):
    wynik = 0
    if temperature_type == "Fahrenheit":
        wynik = (degrees*1.8) + 32
    elif temperature_type == "Rankine":
        wynik = (degrees+273.15)*1.8
    elif temperature_type == "Kelvin":
        wynik = degrees + 273.15
    else:
        print("Podany został błedny typ temperatury")
    return wynik
c = 27
f = temperature_changer("Fahrenheit", c)
k = temperature_changer("Kelvin", c)
r = temperature_changer("Rankine", c)
print("Celcjusz: {} Fahrenheit: {} Rankine: {} Kelvin: {}".format(c, f, r, k))