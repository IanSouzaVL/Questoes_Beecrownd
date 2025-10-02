numeros = []
posicao = 0

for i in range(100):
    valor = int(input())
    numeros.append(valor)

maior = max(numeros)
posicao = numeros.index(maior) + 1

print(maior)
print(posicao)
