#Km percorridos de um carro alugado. Quantidades de dias alugados. 60 reais por dia. 0.15 por km rodado.

kms_inicial = float(input("Qual a KM inicial do carro: "))
kms_final = float(input("Qual a KM final do carro: "))

kms_pecorrido = (kms_final-kms_inicial)
valor_kms_pecorrido = (kms_pecorrido * 0.15)

dias_alugado = int(input("Por quantos dias o carro foi alugado: "))

valor_diaria = (dias_alugado * 60)

valor_total = (valor_kms_pecorrido + valor_diaria)

print("---")
print("Km pecorridos: {}".format(kms_pecorrido))
print("Valor da km: {}".format(valor_kms_pecorrido))
print("---")
print("Dias de aluguel: {}".format(dias_alugado))
print("Valor das diáris: {}".format(valor_diaria))
print("---")
print("Total: {}".format(valor_total))

