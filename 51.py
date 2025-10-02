n = int(input())

i = 0

while  i < n:
    x = int(input())
    if x % 2 == 0:
        if x > 0:
            print("EVEN POSITIVE")
        elif x < 0:
            print("EVEN NEGATIVE")
        else:
            print("NULL")
    else:
        if x > 0:
            print("ODD POSITIVE")
        elif x < 0:
            print("ODD NEGATIVE")
    i += 1