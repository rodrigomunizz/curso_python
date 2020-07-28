#colocar os nomes em uma lista aleatoriamente

import random
nome1 = str(input("Primeiro aluno: "))
nome2 = str(input("Segundo aluno: "))
nome3 = str(input("Terceiro aluno: "))
nome4 = str(input("Quarto aluno: "))

listaAluno = [nome1,nome2,nome3,nome4]

random.shuffle(listaAluno)

print(listaAluno)