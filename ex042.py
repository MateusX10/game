r1 = float(input('Primeiro segmento: '))
r2 = float(input("Segundo segmento: "))
r3 = float(input('Terceiro segmento: '))
if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r2 + r1:
    print('As retas acima NÃO PODEM formar um triângulo')
else:
    print('As retas acima podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print("EQUILATERO")
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print("ISÓSCELES")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
