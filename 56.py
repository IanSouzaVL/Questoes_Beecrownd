n = int(input())


total = 0

coelhos = 0
ratos = 0
sapos = 0


for i in range(1, n + 1):
    entrada = input().split()

    quantidade = int(entrada[0])
    tipo = entrada[1]

    if tipo == "C":
        coelhos += quantidade
    elif tipo == "R":
        ratos += quantidade
    elif tipo == "S":
        sapos += quantidade

    total += quantidade

print(f"Total: {total} cobaias")

print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")

print(f"Percentual de coelhos: {((coelhos / total) * 100):.2f} %")
print(f"Percentual de ratos: {((ratos / total) * 100):.2f} %")
print(f"Percentual de sapos: {((sapos / total) * 100):.2f} %")