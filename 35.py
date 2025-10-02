salario = float(input())

reajuste = {
    0: 0.15,
    400.01: 0.12,
    800.01: 0.10,
    1200.01: 0.07,
    2000.01: 0.04
}

if salario <= 400:
    total_reajuste = salario * reajuste[0]
    percentual = reajuste[0] * 100
elif salario <= 800:
    total_reajuste = salario * reajuste[400.01]
    percentual = reajuste[400.01] * 100
elif salario <= 1200:
    total_reajuste = salario * reajuste[800.01]
    percentual = reajuste[800.01] * 100
elif salario <= 2000:
    total_reajuste = salario * reajuste[1200.01]
    percentual = reajuste[1200.01] * 100
else:
    total_reajuste = salario * reajuste[2000.01]
    percentual = reajuste[2000.01] * 100

novo_salario = salario + total_reajuste
print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {total_reajuste:.2f}")
print(f"Em percentual: {percentual:.0f} %")