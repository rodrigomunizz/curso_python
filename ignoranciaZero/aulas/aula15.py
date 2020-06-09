n = int(input("Digite o numero de pessoas: "))

cont = 0

while cont < n:

    dia = int(input("Digite o dia de nascimento da pessoa %i: "%(cont+1)))
    mes = int(input("Digite o mes de nascimento da pessoa %i: "%(cont+1)))
    ano = int(input("Digite o ano de nascimento da pessoa %i: "%(cont+1)))
    idade = int(input("Digite a idade a ser completada da pessoa %i: "%(cont+1)))

    print("A pessoa %i fara %i anos no dia %d/%i/%d" %(cont+1, idade, dia, mes, ano+idade))

    cont += 1

#Para inteiros --> %i ou %d
#Colocar % --> %%

###########################################################

"""
Queremos números naturais que sejam produtos de três
números consecutivos

Exemplo: 120 é procurado, pois 4.5.6 == 120.
Dado um inteiro não-negativo n, verificar se n é procurado.
"""
#40 ?
# 1 X 2 X 3 == 6
# 2 X 3 X 4 == 24
# 3 X 4 X 5 == 60

#120
# 1 X 2 X 3 == 6
# 2 X 3 X 4 == 24
# 3 X 4 X 5 == 60
# 4 X 5 X 6 == 120

num = int(input("Digite um numero: "))

i= 1

while i * (i + 1) * (i + 2) < num:
    i += 1

if i * (i + 1) * (i + 2) == num:
    print(num, "é procurado")
else:
    print(num, "não é procurado")