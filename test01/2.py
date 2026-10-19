#slovník
kontakty = {
    "jmeno": "Jan",
    "prijmeni": "Novak",
    "vek": 30
    "email": "jan.movak6321@antimail.cx"
    "telefon": "6968676564636261"
}
#vypíše celou satovou strukturu
print(f"Puvodni Kontakty: {kontakty}")

print(f"Jmeno: {kontakty['jmeno']}")

kontakty["vek"] = 69
print(kontakty["vek"])

kontakty["mesto"] = "Most"
print(kontakty)

telefon = kontakty.get("telefon")
print("Telefoni cislo: (telefon)")