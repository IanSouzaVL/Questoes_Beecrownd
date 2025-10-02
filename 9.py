numero = int(input("Digite o número do funcionário: "))
horas = float(input("Digite o número de horas trabalhadas: "))  
valor_hora = float(input("Digite o valor por hora: "))

salary = horas * valor_hora 

print("NUMBER =", numero)
print(f"SALARY = U$ {salary:.2f}")
