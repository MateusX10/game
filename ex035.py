import colorama
colorama.init()
print('========= ANALISADOR DE TRIÂNGULOS! =============')
seg1 = float(input("Medida do primeiro segmento: "))
seg2 = float(input("Medida do segundo segmento: "))
seg3 = float(input("Medida do terceiro segmento: "))
if seg1 > seg2 + seg3 or seg2 > seg1 + seg3 or seg3 > seg1 + seg2:
    print('\033[31mOs segmentos acima NÃO PODEM formar um triângulo!')
else:
    print('\033[34mOs segmentos acima PODEM formar um triângulo!')