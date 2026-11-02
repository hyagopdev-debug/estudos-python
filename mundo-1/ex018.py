from math import cos, sin, tan, radians
angulo = float(input("Digite o ângulo em graus que deseja: "))
radiano = radians(angulo)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)
print(f"O ângulo de {angulo} tem o SENO de {seno:.2f}")
print(f"O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}")
print(f"O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}")