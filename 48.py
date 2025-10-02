x = int(input())
y = int(input())

inicio = min(x, y) + 1
fim = max(x, y)

impares = []

total = 0

for i in range(inicio, fim):
    if i % 2 != 0:
        total += i

print(total)