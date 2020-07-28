#Programa para calcular seno, cosseno, tangente - em cima de um angulo

import math

ang = float(input('Digite um angulo que você deseja: '))

angrad = math.radians(ang)

sen = math.sin(angrad)
cos = math.cos(angrad)
tan = math.tan(angrad)

print("Angulo {} - Seno {} - Cosseno {} - Tangente {}.".format(ang,sen,cos,tan))


