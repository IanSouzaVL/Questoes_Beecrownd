numeros = []
positivos = 0

for i in range(6):
    valor = float(input())
    
    if valor > 0:
        positivos += 1
        numeros.append(valor)

print(f"{positivos} valores positivos")

media = sum(numeros) / len(numeros)

print(f"{media:.1f}")