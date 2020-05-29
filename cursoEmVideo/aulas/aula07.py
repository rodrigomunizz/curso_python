primeironumero = int(input('Primeiro numero: '))
segundonumero = int(input('Segundo numero: '))

print(type(primeironumero))

soma = primeironumero + segundonumero
subtracao = primeironumero - segundonumero
multiplicacao = primeironumero * segundonumero

print(soma)
print(subtracao)
print(multiplicacao)
print('Divisão é {}'.format(primeironumero / segundonumero))
print('Potencia é {}'.format(primeironumero ** segundonumero))
print('Divisao inteira é {:.3f}'.format(primeironumero // segundonumero))
print('Resto da divisão é {}'.format(primeironumero % segundonumero))

# \n - quebrar linha
# , end= '' para manter a mesma linha

# + adição
# - subtração
# * multiplicação
# / divisão
# ** potencia
# // divisão inteira
# % resto da divisão

# order de precedencia
# () -> ** -> * / // % -> + -

nome = input('Qual é o seu nome ? ')

# valor dentro do {} é espaçamento
print("Centralizado a direita {:>35} ".format(nome))
print("Centralizado {:^35} ".format(nome))
print("Centralizado a esquerda {:<35} ".format(nome))
