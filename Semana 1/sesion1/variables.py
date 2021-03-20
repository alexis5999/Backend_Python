nombre = input("ingrese su nombre")
edad = input("ingrese su Edad")
ecivil = input("Estado Civil")
if ecivil == "C":
    valorec = "CASADO"
elif ecivil == "V":
    valorec = "VIUDO"
elif ecivil == "":
    valorec = "DIVORCIADO"
else:
    valorec = "SOLTERO"
print("hola", nombre, "Su estado civil es:", valorec)
print(" hola como estan todos aqui")



