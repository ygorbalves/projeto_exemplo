valores = input().split()
#Calcule quantidade de litros necessária para realizar a viagem e imprima com TRÊS dígitos após o ponto decimal
tempo_gasto = int(valores[0])
vel_media= int(valores[1])
CONSUMO_CARRO = 12
litros_combustivel = tempo_gasto*vel_media/CONSUMO_CARRO
print(f"{litros_combustivel:.3f}")