import colorama
colorama.init()
num = int(input("Digite um número qualquer: "))
if num % 2 == 0:
    print(f'O número {num} é \033[34mpar!\033[m')
else:
    print(f'O número {num} é \033[34mímpar!\033[m')