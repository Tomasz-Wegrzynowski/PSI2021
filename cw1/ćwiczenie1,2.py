x = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
print(x)

liczba_liter1 = 0
liczba_liter2 = 0

for i in range(len(x)):
    if (x[i] == "a"):
        liczba_liter1 = liczba_liter1 + 1
    if (x[i] == "l"):
        liczba_liter2 = liczba_liter2 + 1
print(f'W tekście jest {liczba_liter1} liter a oraz {liczba_liter2} liter l')