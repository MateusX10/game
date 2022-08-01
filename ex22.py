from time import sleep
nome = str(input("Digite seu nome completo: ")).strip()
maiúsculas = nome.upper() 
minúsculas = nome.lower()
tamanho = len(nome.strip()) - nome.count(" ")
dividido = nome.split()
primeiro_nome = dividido[0]
print('Análisando o seu nome...')
sleep(1.3)
print(f'''Seu nome em maiúsculas é '{maiúsculas}' \nSeu nome em minúsculas é '{minúsculas}'
Seu nome tem ao todo {tamanho} letra(s)
Seu primeiro nome é '{primeiro_nome}' e ele tem {len(primeiro_nome)} letra(s)''')