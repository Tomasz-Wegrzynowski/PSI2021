




def calc(temperature_type):
    print("Podaj temperature w Celsjuszach:")
    temp = input()
    temp = int(temp)
    if temp > 51 or temp < -51:
        print("To chyba nie celsjusz!")
    else:
        print("To jest celsjusz:",temp)
    # print("Podaj typ temperatury na jaki chcesz przeliczyć Celsjusza. Do wyboru Fahrenheit(H), Rankie(R), Kelvin(K). Wciśnij literkę.")
    # temperature_type = input()
    # temperature_type = str(temperature_type)
    if temperature_type == "H":
        print(("Skala Fahrenheita " + str(temp*9)/5+32))
    elif temperature_type == "R":
        print(((("Skala Rankie " + str(temp+273.15)*9)/5)))
    elif temperature_type == "K":
        print("Skala Kelvina " + str(temp+273.15))
    else:
        print("Nie ma takiej wartości!")
calc("K")



