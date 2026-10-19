cislo_list = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,7]
unikatni_cisla = set(cislo_list)
print("Unikatni cisla:", unikatni_cisla)
print("Puvodni seznam:", cislo_list)

prazdna_mnoz = set()
prazdna_mnoz.add(69)
prazdna_mnoz.add(0)
prazdna_mnoz.add(698752489)

print("Mnozina po pridani prvku:", prazdna_mnoz)

if 3 in unikatni_cisla:
    print("Cislo 3 je v mnozine unikatnich cisel.")
else:
    print("cislo 3 není v mnozine unikatnich cisel.")