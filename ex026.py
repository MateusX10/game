frase = str(input("Digite uma frase: ")).lower().strip()
quantas_letras_a = frase.count("a")
primeira_letra_a = frase.find("a")
ultima_letra_a = frase.rfind("a")
print(f'''A letra "A" aparece {quantas_letras_a} vezes
A primeira letra "A" apareceu na posição {primeira_letra_a + 1} e a última na posição {ultima_letra_a + 1}''')