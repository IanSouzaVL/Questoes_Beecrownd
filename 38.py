salario = float(input())

if salario <= 2000:
    print("Isento")

elif salario <= 3000:
    imposto_total = (salario - 2000) * 0.08
    print(f"R$ {imposto_total:.2f}")

elif salario <= 4500:
    imposto_total = (salario - 3000) * 0.18 + (1000 * 0.08)
    print(f"R$ {imposto_total:.2f}")

else:
    imposto_total = (salario - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
    print(f"R$ {imposto_total:.2f}")