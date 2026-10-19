cislo = 68

#% je modulo, vraci zbytek po deleni
if cislo % 2 == 0:
    print("cislo je sude")
else:
    print("cislo je liche")

print(7 % 2)











nakupni_kosuik = []

if nakupni_kosuik:
    print("Kosik neni prazdny")
else:
    print("kosik je prazdny")


povolene_ovoc = ["jelko", "banan", "manga"]
moje_ovoc = "manga"

if moje_ovoc in povolene_ovoc:
    print(f"{moje_ovoc.capitalize()} je povolene ovoce")
else:
    print(f"{moje_ovoc.capitalize()} neni na seznamu povolenyvch ovocu")