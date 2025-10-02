dia_inicial = input().split()
dia_inicial = int(dia_inicial[1])

instante_inicial = input().split(" : ")
hora_inicial = int(instante_inicial[0])
minuto_inicial = int(instante_inicial[1])
segundo_inicial = int(instante_inicial[2])

dia_final = input().split()
dia_final = int(dia_final[1])

instante_final = input().split(" : ")
hora_final = int(instante_final[0])
minuto_final = int(instante_final[1])
segundo_final = int(instante_final[2])

tempo_inicial = (dia_inicial * 86400) + (hora_inicial * 3600) + (minuto_inicial * 60) + segundo_inicial
tempo_final = (dia_final * 86400) + (hora_final * 3600) + (minuto_final * 60) + segundo_final

duracao = tempo_final - tempo_inicial

w = duracao // 86400
resto = duracao % 86400

x = resto // 3600
resto = resto % 3600

y = resto // 60
resto = resto % 60

z = resto

print(f"{w} dia(s)")
print(f"{x} hora(s)")
print(f"{y} minuto(s)")
print(f"{z} segundo(s)")