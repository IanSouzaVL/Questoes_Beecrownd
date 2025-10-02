x = int(input())
impares = []
q = 0

while q < 6:
    if x % 2 != 0:
        q += 1
        impares.append(x)
    x += 1

for i in range(len(impares)):
    print(impares[i])
    