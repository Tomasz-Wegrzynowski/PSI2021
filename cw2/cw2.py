
slowo = "dog"

def przyjmij(data_text):
    slownik =  {"lenght": print(len(slowo)),
                "letters": letters(slowo),
                "big_letters": print(slowo.upper()),
                "small_letters": print(slowo.lower())
    }


def letters(slowo):
    for znak in slowo:
        print(znak)

przyjmij(slowo)
