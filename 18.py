tempo = float(input("Tempo gasto na viagem (horas): "))
velocidade = float(input("Velocidade média (km/h): "))
distancia = tempo * velocidade
litros = distancia / 12
print(f"{litros:.3f}")