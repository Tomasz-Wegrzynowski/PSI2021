studenci = dict([("111000", "Jan Kowalski"), ("222000", "Jarosław Nowak"), ("303030", "Mikołaj Perez")])
nauczyciele = dict([("789213", "Kazimierz Siemowuj"), ("876212", "Olaf Bodek"), ("378921", "Henryk Krzesiński")])

ludzie = [studenci, nauczyciele]
ciag = str(ludzie).replace("[", "")
usuniete_znaki = "{}[]''"

for character in usuniete_znaki:
	ciag = ciag.replace(character, "")
print(ciag)