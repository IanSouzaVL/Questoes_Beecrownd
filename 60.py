i = 0.0

while i <= 2.0:
    j = i + 1.0
    c = 0
    while c < 3:
        if i == int(i):
            str_i = str(int(i))
        else:
            str_i = f"{i:.1f}"
        if j == int(j):
            str_j = str(int(j))
        else:
            str_j = f"{j:.1f}"
        print(f"I={str_i} J={str_j}")
        j += 1.0
        c += 1
    i += 0.2
    i = round(i, 1)
