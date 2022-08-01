mai = men = 0
for v in range(1,4):
    n = int(input("Digite um valor: "))
    if mai == 0 and men == 0:
        mai = men = n
    else:
        if n > mai:
            mai = n
        if n < men:
            men = n
print(f'O maior valor digitado foi {mai} e o menor foi {men}')