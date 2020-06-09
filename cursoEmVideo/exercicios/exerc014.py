# Converter de grau C para F

grau_celsius = int(input("Qual o grau Celsius você deseja converter: "))

grau_fah = ((grau_celsius * (9/5)) + 32)

print("{:.2f}ºC equivale a {:.2f}ºF.".format(grau_celsius,grau_fah))