def funkcja(text, letter):
    text = text.replace(letter, "")
    return text

tekst = "ada ma kota i tak to jest"
print(funkcja(tekst, "a"))

