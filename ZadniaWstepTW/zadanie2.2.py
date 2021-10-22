def funkcja(data_text):
     slownik = {"lenght" : len(data_text),
                "letters" : convert(data_text),
                "big_letters" : data_text.upper(),
                "small_letters" : data_text.lower()}
     return slownik

def convert(text):
     lista=[]
     lista[:0] = tekst
     return lista

tekst = "dog"
info = funkcja(tekst)
print(info)