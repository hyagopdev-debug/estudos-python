from math import hypot
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digete o compriemnto do cateto adjacente: "))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f"A hipotenusa vai medir {hipotenusa:.2f}")