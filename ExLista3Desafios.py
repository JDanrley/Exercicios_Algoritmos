#Exercício 1:

print ('Ex 1: Análise para verificar se o número digitado é triangular.\n')

n = int(input('Digite o número que será analisado: '))
x = 1
flag = False
while x <= n:
  if x * (x + 1) * (x + 2) == n: #Analisando se algum trio de números inteiros subsequentes se iguala ao valor inserido.
    flag = True
    a, b, c = x, (x + 1), (x + 2)
  x += 1
if flag:
  print (f'O número é triangular, pois {a}x{b}x{c} = {n}')
else:
  print ('O número não é triangular')

#Exercício 2:

print ('\nEx 2: Troco do cliente.')

preço = int(input('Insira o valor da conta do cliente: '))
pag = int(input('Insira o valor do pagamento realizado: '))
troco = pag - preço
if preço != pag:
  n50 = troco // 50
  n20 = (troco - (n50*50)) // 20 
  n10 = (troco - (n50*50 + n20*20)) // 10
  n5 = (troco - (n50*50 + n20*20 + n10*10)) // 5
  n2 = (troco - (n50*50 + n20*20 + n10*10 + n5*5)) // 2
  n1 = troco - (n50*50 + n20*20 + n10*10 + n5*5 + n2*2)
  print(f'O troco de R${troco},00 será composto com as seguintes notas: \n\n{n1} Notas de 1 real.\n{n2} Notas de 2 Reais.\n{n5} Notas de 5 Reais.\n{n10} Notas de 10 Reais.\n{n20} Notas de 20 Reais.\n{n50} Notas de 50 Reais')
else:
  print("Não será necessário nenhum troco!")

#Exercício 3:

print('\nEx 3: Análise para verificar se o número inserido é ou não primo.')

n = int(input('Insira um número inteiro e positivo a ser analisado: '))
i = n - 1
if n == 1 or n == 0:
  print('O valor não é válido, digite um número maior que 1')
  i = 0
primo = 1
while i >= 2:
  flag = n % i
  i -=1
  if flag == 0:
    primo = False
if not primo and i != 0:
  print('O número não é primo')
elif i != 0:
  print('O número é primo')

#Exercício 4:

print('\nEx 4: Decomposição em fatores primos e cálculo de multiplicidade.\n')

n = int(input('Insira um número inteiro e positivo a ser decomposto: '))
nf = n
if n < 1:
    print('Valor inválido. Insira um número positivo e superior à 1 (um).')
else:
    decom = ''
    i = 2 #Valor definido por ser o menor primo existente
    while n != 1:
        if n % i == 0:
            n = n / i
            decom = decom + str(i)
        else:
            i += 1
    print (f'Decomposição do {nf}\n')
    
    i = 0
    while i < len(decom):
        mult = decom[i] #mantendo a variável "mult" para ter o valor na tela do usuário
        mult2 = int(decom.count(mult)) #Definindo a posição no vetor para realizar contagem e definir multiplicidade
        mult = int(mult) #Transformando o elementos selecionado na string em número inteiro para operações na impressão
        print (f'{i + 1}º Fator de decomposição: {mult}\n{nf} divido por {mult} = {int(nf / mult)}\nMultiplicidade do fator {mult} = {mult2}\n')
        nf = nf / mult
        i += 1   

#Exercício 5:

print ('\nEx 5: Inverter as algarismos de um número.\n')

n = input('Insira o número a ser invertido: ')
x = len(n)
final = ''
while x > 0:
  final = final + n [x - 1]
  x -= 1
print (f'O número invertido: {int(final)}')
