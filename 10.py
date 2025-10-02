nome = input()
salaFixo = float(input())
vendas = float(input())

comissao = vendas * 0.15
total = salaFixo + comissao

print(f"TOTAL = R$ {total:.2f}")
