#generátorová rotace

#Vytvoření seznamu čtverců číseo od 0 do 9
squares = [x**2 for x in range (10)]
print(f"Čtverce čísel od 0 do 9: {squares}")

mocnina = []
for x in range(10):
    mocnina.append(x**2)
    print(x, "2. mocnia tohoto čísla je:", x**2)

mocnina3 = []
for y in range(10):
    mocnina3.append(x**3)
    print(y, "3. mocnia tohoto čísla je:", x**3)


word2 = ["Python", "je", "skvělý", "programovací", "jazyk"]
upper_words = [word.upper() for word in word2]
print(f"Slova převedená na CPASLOCK: {upper_words}")