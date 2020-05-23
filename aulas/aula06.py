primeironumero = int ( input ('Primeiro numero: ') )
print(type(primeironumero))

segundonumero = int ( input ('Segundo numero: ') )

soma = (primeironumero + segundonumero)

# int - positivos e negativos
# float - numeros com pontos flutuantes - numero real
# bool - True - False
# str - palavras em aspas

print ('A soma é ',soma)
print ('===========')
print ('A some é {}'.format(soma))
print ('===========')
print ('A soma entre ',primeironumero, ' e ',segundonumero,' - vale : ', soma)
print ('===========')
print ('A soma entre {} e {} - vale: {}'.format(primeironumero, segundonumero, soma))