mai = 0
for v in range(1,3):
    n = int(input(f"Digite o {v}º valor: "))
    if mai == 0:
        mai = n
    else:
        if n > mai:
            print("O SEGUNDO valor é o maior")
        elif n == mai:
            print("AMBOS os valores são idênticos")
        else:
            print("O PRIMEIRO valor é o maior")
