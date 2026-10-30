dia = int(input("Digite quantos dias você usou o carro:"))
km = float(input("Digite quantos km você andou com o carro:"))
preco_dia = dia * 60 
preco_km = dia * 0.15
preco_total = preco_dia + preco_km 
print(f"O total a pagar é {preco_total:.2f}")