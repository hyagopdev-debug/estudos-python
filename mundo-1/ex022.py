nome = str(input("Digite seu nome completo: "))

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
quantidade = len(nome.replace(" ", ""))
nome_1 = nome.split()[0]
quantidade_1 = len(nome_1)

print(nome_maiusculo)
print(nome_minusculo)
print(quantidade)
print(quantidade_1)