import colorama
colorama.init()
média = 0
for v in range(1,3):
    nota = float(input(f"{v}º nota do aluno: "))
    média += nota
média = média / 2
print(f"Sua média final foi de {média:.1f}.")
if média >= 70:
    print(f'\033[32mAPROVADO!\033[m')
elif 50 <= média < 70:
    print(f'\033[33mRECUPERAÇÃO!\033[m')
else:
    print("\033[31mREPROVADO!\033[m")