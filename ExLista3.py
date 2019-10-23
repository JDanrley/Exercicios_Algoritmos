#Lista de Exercícios 3:
#Exercício 1:

print ('\nExercício 1 - Solicitar uma nota entre zero e dez, e solicitar novamente caso valor seja inválido.\n')

nota = - 1
while nota > 10 or nota < 0:
    nota = int(input('Insira uma nota entre zero e dez: '))
    if nota > 10 or nota < 0:
        print ('ERRO: Valor inválido')
    else:
        print (f'A nota inserida {nota} é válida e foi armazenada')
        
#Exercício 2:

print ('\nExercício 3 - Solicitar username e senha, e solicitar novamente caso estes sejam iguais.\n')

user = 0
senha = 0
while user == senha:
    user = str (input('Insira o nome de usuário a ser utilizado: '))
    senha = str(input('Insira uma nova senha: '))
    if user != senha:
        print (f'A senha para o usuário "{user}" é válida e foi armazenada.')
    else:
        print ('A senha é inválida, ela não pode ser igual ao usuário. Tente novamente abaixo.')

#Exercício 3:

print ('\nExercício 3 - Cálculo para quantidade de anos necessários para que população de país A ultrapasse a do país B.\n')

pa, pb, ca, cb = 80000, 200000, 1.03, 1.015
i = 0
while pa <= pb:
    pa, pb, = pa * ca, pb * cb
    i += 1
print (f'Serão necessários {i} anos para a população do país A ultrapassar a do país B')

#Exercício 4:

print ('\nExercício 4: Definir número referente à sua posição na sequência de Fibonacci.\n')

n = int(input('Insira o número: '))

a = 1
b = 1
c = 0
i = 2 #Contador começa em 2, pois os dois primeiros casos são exceções e devem ser pulados.
if n == 1 or n == 2: #Definindo exceção dos dois primeiros casos, n = 1 e n = 2.
    c = 1
else:
    while i < n:
        c = a + b #Posição a, b e c representam valores do anterior 1, anterior 2 e resultado da soma.
        copyb = b #Definindo uma cópia de 'b' para poder realocar o valor posteriormente.
        b = c
        a = copyb
        i += 1
        
print (f'O número na posição {n} na sequência de Fibonacci é igual à {c}.')

#Exercício 5:

#Exercício 5:

print ('\nExercício 5: Determinar o MDC de dois números inseridos pelo usuário, pelo algoritmo de Euclides. \n')

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
copy1 = n1
copy2 = n2
resto = 1
while True:
    if resto == 0:
        break
    resto = n1 % n2 #Realizando determinar do resto, para ser o próximo divisor.
    n1, n2 = n2, resto #Atribuindo as posições corretas
print (f'O MDC ({copy1},{copy2}) = {n1}') #O último divisor antes de n2 receber "Zero", na linha anterior n1 = n2, logo, MDC = n1
