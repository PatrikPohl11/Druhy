for i in range(10):
        print(f"Druha mocnina {i} je {i**2}")


jazyky = ["cz", "pl", "slo", "ger", "nig", "chor",]

for jazyk in jazyky:
    print(f"ucim se jazyky: {jazyk}")






for i in range(2, 10):
    for x in range(2, i):
            print(f"kontroluju cislo {i} delene {x}")
            if i % x ==0:                   #modulo, zbytek po deleni
                  break
    else:
            print(f"{i} ===========je prvocislo==============")






#bubliny
import random
velikost = 10
pole = [random.randint(1, 100) for i in range(velikost)]
print(f"Neusporadane pole: {pole}")

for i in range (velikost -1 ,0, -1):
      for j in range (0,i):
        if pole[j] > pole[j+1]:
                pole[j], pole[j+1] = pole[j+1], pole[j]
print(f"serazene pole: {pole}")