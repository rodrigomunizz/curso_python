salario = float(input("Qual é o seu salário: "))
aumento = float(input("Qual é o seu aumento em %: "))

salario_aumento = (salario*aumento)/100
novo_salario = salario + salario_aumento

print("Seu salario de {:.2f}, com {:.2f}% de aumento é de {:.2f}.".format(salario,aumento,novo_salario))
print("O aumento foi de {:.2f}.".format(salario_aumento))
