entrada = list(map(int, input().split()))

hi, mi, hf, mf = entrada

instante_inicial = (hi * 60) + mi
instante_final = (hf * 60) + mf

if instante_final <= instante_inicial:
    duracao = (24 * 60 - instante_inicial) + instante_final
else:
    duracao = instante_final - instante_inicial

print(f"O JOGO DUROU {duracao//60} HORA(S) E {duracao % 60} MINUTO(S)")