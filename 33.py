hi, hf = map(int, input().split())

if hi < hf:
    duracao = hf - hi
    print(f"O JOGO DUROU {duracao} HORA(S)")
else:
    duracao = (24 - hi) + hf
    print(f"O JOGO DUROU {duracao} HORA(S)")