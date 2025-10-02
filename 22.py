valor = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
print("NOTAS:")
resto = valor
for nota in notas:
    qtd = int(resto // nota)
    print(f"{qtd} nota(s) de R$ {nota:.2f}")
    resto -= qtd * nota
print("MOEDAS:")
resto = round(resto, 2)
centavos = int(round(resto * 100))
moedas_centavos = [100, 50, 25, 10, 5, 1]
for i, moeda in enumerate(moedas_centavos):
    qtd = centavos // moeda
    print(f"{qtd} moeda(s) de R$ {moedas[i]:.2f}")
    centavos -= qtd * moeda