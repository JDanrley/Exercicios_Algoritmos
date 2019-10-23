#Lista de exercícios 2:
#Exercício 1:

print ('Definir o tipo do triângulo - Ex 1 da segunda lista.')

l1 = int(input('Insira o tamanho do primeiro lado: '))
l2 = int(input('Insira o tamanho do segundo lado: '))
l3 = int(input('Insira o tamanho do terceiro lado: '))

if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l2 + l1 or l1 < l2 - l3 or l2 < l1 - l3 or l3 < l2 - l1 or l1 < l3 - l2 or l2 < l3 - l1 or l3 < l1 - l2: #Condições de relação para a existência de um triângulo.
    print ('Os valores inseridos não atendem à condição de existência de um triângulo')
elif l1 != l2 and l1 != l3 and l2 != l3:
    print ('Os valores inseridos são de um triângulo escaleno')
elif l1 == l2 and l1 == l3:
    print ('O valores inseridos são de um triângulo equilátero')
else:
    print ('Os valores inseridos são de um triângulo isósceles')

#Exercício 2:
    
print ('Determinar se um ano é bissexto - Ex 2 da segunda lista.')

ano = int(input('Insira o ano a ser calculado: '))
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print ('O ano é bissexto')
else:
    print ('O ano não é bissexto')

#Exercício 3:
    
print ('Programa de cálculo do João Pao-de-Pescador - Ex 3 da segunda lista.')

excesso = 0
multa = 0

peso = float(input('Insira o valor pesado, em kg: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print (f'O peso extrapolou o valor máximo em {excesso:.2f}kg\nO valor da multa ficou em R${multa}')
else:
    print (f'Excesso: {excesso}\nMulta: {multa}')

#Exercício 4:
    
print ('Definir o maior de três números - Ex 4 da segunda lista.')

n1 = int(input('OBS: Insira apenas valores diferentes \nInsira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

if n1 > n2 and n1 > n3:
    print (f'O {n1} é o maior número inserido')
elif n2 > n1 and n2 > n3:
    print (f'O {n2} é o maior número inserido')
elif n3 > n2 and n3 > n1:
    print (f'O {n3} é o maior número inserido')
else:
    print ('Dados inválidos, os números de maior valor são iguais')

#Exercício 5:
    
print ('Definir o maior e o menor de três números - Ex 5 da segunda lista.')

n1 = int(input('OBS: Insira apenas valores diferentes \nInsira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

if n1 > n2 and n1 > n3:
    major = n1
elif n2 > n1 and n2 > n3:
    major = n2
elif n3 > n2 and n3 > n1:
    major = n3
if n1 < n2 and n1 < n3:
    minor = n1
elif n2 < n1 and n2 < n3:
    minor = n2
elif n3 < n2 and n3 < n1:
    minor = n3

print (f'Número de maior valor {major}\nNúmero de menor valor: {minor}')

#Exercício 6:

print ('Cálculo de salário bruto e líquido - Ex 6 da segunda lista.')

sal = float(input('Insira o preço da sua hora de trabalho: '))
hr = float(input('Digite a quantidade de horas trabalhadas no mês: '))
salb = sal * hr
ir = salb * 11 / 100
inss = salb * 8 / 100
sind = salb * 5 / 100
saliq = salb - ir - inss - sind
print (f'a. + Salário Bruto: R${salb} \nb. - IR (11%): R${ir} \nc. - INSS (8%): R${inss} \ne. = Salário líquido: R${saliq}')

#Exercício 7:

print ('Cálculo da quantidade e preço da tinta - Ex 7 da segunda lista.')

metros = int(input('Insira a quantidade de metros quadrados a ser pintada: '))

if metros % (18 * 3) == 0: #Calculando cenário para consumo total da tinta
    latas = metros / 54
else:
    latas = int(metros / 54) + 1 #Calculando cenário para consumo parcial de uma das latas
print (f'A quantidade de latas utilizadas é {latas}.\nO preço desta mercadoria ficou em R${latas*60},00')
