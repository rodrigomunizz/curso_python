import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto afjacente: '))

hip = (((co**2) + (ca**2)) ** (1/2))

hip2 = math.hypot(co,ca)

print("{:.2f}".format(hip))
print("{:.2f}".format(hip2))
