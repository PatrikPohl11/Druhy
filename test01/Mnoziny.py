python_devs = {"ChatGPT", "Jirka", "Indian", "Cypek", "Typek"}
java_devs = {"Nevim", "Nevim2", "Nevim_uz_zase", "Indian", "ChatGPT"}

# operace sjednoceni
vsichni_devs = python_devs | java_devs
print("Vsichni vyvojari (sjednoceni):", vsichni_devs)

#operace pruniku (A)
polygot_devs = python_devs & java_devs
print("Vyvojari kteri umi oboje (pruinik):", polygot_devs)