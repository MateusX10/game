distância_viagem = float(input("Ditância da viagem (em Km): "))
custo_viagem = distância_viagem * 0.45 if distância_viagem > 200 else distância_viagem * 0.50
print(f'Você está prestes a começar uma viagem de de {distância_viagem:.1f}Km')
print(f'E o preço da sua passagem será de R${custo_viagem:.2f}')