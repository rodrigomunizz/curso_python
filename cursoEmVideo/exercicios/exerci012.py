#Desconto de um valor em cima de uma porcentagem

valor = float(input("Digite o valor que você quer o desconto - "))
desconto = float(input("Digite o valor do desconto - "))

descontofinal = ((valor*desconto)/100)
valorfinal = (valor - descontofinal)

print('Aplicando um desconto de {}% em cima de {} - fica {} de desconto, totalizando {}.'.format(desconto, valor, descontofinal, valorfinal))


