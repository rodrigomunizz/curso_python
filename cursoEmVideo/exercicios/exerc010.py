print('Programa que converte real para dolar')
valdolar=float(input('Qual o valor de um real em dolar hoje? - $'))
temreal=float(input('Qual o valor real você quer converter? - R$'))

print('R${} equivale a ${:.2f}'.format(temreal,(temreal*valdolar)))
