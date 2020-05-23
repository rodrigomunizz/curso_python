Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> //teste
SyntaxError: invalid syntax
>>> 
>>> print("Teste")
Teste
>>> print('Olá, Mundo!')
Olá, Mundo!
>>> print(7)
7
>>> print('7')
7
>>> print(7+4)
11
>>> print('7+4='7+4)
SyntaxError: invalid syntax
>>> print('7+4='+7+4)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print('7+4='+7+4)
TypeError: can only concatenate str (not "int") to str
>>> print(('7+4='+(7+4));
      
SyntaxError: invalid syntax
>>> print((7+4))
11
>>> print(('7+4=',7+4);
      
SyntaxError: invalid syntax
>>> print('7+4=' , 4)

7+4= 4
>>> print('7+4=' , 7+4)
7+4= 11
>>> print('7+4 = ' , 4)
7+4 =  4
>>> print('7+4 = ' , 7+4)
7+4 =  11
>>> nome = 'Rodrigo'
>>> idade = 35
>>> peso = 80
>>> print (nome, idade, peso)
Rodrigo 35 80
>>> nome = input('Qual é o seu nome?)
	     
SyntaxError: EOL while scanning string literal
>>> nome = input('Qual é o seu nome?')
Qual é o seu nome? Rodrigo
>>> idade = input('Quantos anos vc tem ?')
Quantos anos vc tem ?35
>>> print (nome, idade)
 Rodrigo 35
>>> 