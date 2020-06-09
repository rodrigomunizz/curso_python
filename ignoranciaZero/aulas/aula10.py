# idade = int(input("Digite sua idade: "))
#
# if 18 <= idade < 70:
#     print("Você pode receber o benefício")
# else:
#     print("Você não pode receber o benefício")

"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
usuário o valor do saque e depois informar quantas notas de cada valor
serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na
máquina.
	Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
	notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

	Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
	três notas de 100, uma nota de 50, quatro notas de 10,
	uma nota de 5 e quatro notas de 1.
// %
"""
saque = int(input("Quer sacar qual valor? ´- "))

notas100 = saque // 100;
notas50 = (saque - (notas100 * 100)) // 50
notas10 = (saque - (notas100 * 100) - (notas50 * 50)) // 10
notas05 = (saque - (notas100 * 100) - (notas50 * 50) - (notas10 * 10)) // 5
notas01 = (saque - (notas100 * 100) - (notas50 * 50) - (notas10 * 10) - (notas05 * 5)) // 1

if 10 < saque < 601:
    print(notas100)
    print(notas50)
    print(notas10)
    print(notas05)
    print(notas01)
else:
    print("Valor não suportado")
