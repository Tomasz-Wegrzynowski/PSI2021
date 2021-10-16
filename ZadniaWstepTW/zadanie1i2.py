zmienna = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
print(zmienna)
liczbalitery1 = 0
liczbalitery2 = 0
for i in range(len(zmienna)):
    if(zmienna[i]=="o"):
        liczbalitery1 = (liczbalitery1 + 1)
    if(zmienna[i]=="g"):
        liczbalitery2 = (liczbalitery2 + 1)

print("W tekście jest {0} liter o oraz {1} liter g".format(liczbalitery1, liczbalitery2))