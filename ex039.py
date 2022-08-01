from datetime import date
ano_nascimento = int(input("Ano de nascimento: "))
atual = date.today().year
idade = atual - ano_nascimento
ano_alistamento = 0
if idade < 18:
    falta = 18 - idade
    ano_alistamento = atual + falta
    print(f'Ainda faltam {falta} ano(s) para seu alistamento, ele será em {ano_alistamento}')
elif idade > 18:
    passou = idade - 18
    ano_alistamento = atual - passou
    print(f'Seu ano de alistamento foi há {passou} ano(s), em {ano_alistamento} ')
else:
    print(f'Esse é o ano de seu alistamento, você deve se alistar IMEDIATAMENTE!')