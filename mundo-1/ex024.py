cidade = str(input("Digite o nome de uma cidade: ")).strip()
comeca_com_santo = cidade.upper().startswith("SANTO")
if comeca_com_santo:
    print("A cidade começa com SANTO!")
else:
    print("A cidade não começa com SANTO!")