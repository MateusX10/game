from datetime import date
ano_nascimento = int(input("Ano de nascimento: "))
atual = date.today().year
idade = atual - ano_nascimento
print(f'O atleta tem {idade} anos')
print("CLASSIFICAÇÃO: ",end='')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JUNIOR")
elif idade <= 25:
    print("SÊNIOR")
else:
    print("MASTER")