#Programa para calcular a quantidade de tinta a ser usada numa parede.

larg=float(input('Digite a largura da parede - '))
altu=float(input('Digite a altura da parede - '))

areaparede = (larg*altu)
tintanecessaria = (areaparede / 2)

print('Largura {}, Altura {}.'.format(larg,altu))
print('Sua area e´de {}m².'.format(areaparede))
print('Necessario(s) {}litro(s) de tinta'.format(tintanecessaria))
