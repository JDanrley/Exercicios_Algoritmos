#Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
#as funções max e min.
print ('Lista IV de exercícios\nAluno José Danrley da Silva\n\n')
print ('Exercício 1)\n\n')
import random #importando biblioteca random

lista = []
for i in range (10):
    lista.append(random.randint(1,100)) #Adicionando elementos à lista
major = 0
minor = 100
for j in range (len(lista)):
    if lista[j] > major:
        major = lista [j]
    if lista[j] < minor:
        minor = lista[j]
        
print (f'Lista: {lista}\nMenor número da lista: {minor}\nMaior número da lista: {major}\n')

#Exercício 2 - Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.

print ('\nExercício 2)\n\n')

import random 

lista = []
for i in range (20):
    lista.append(random.randint(1,100))
par = []
impar = []
i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        par.append(lista[i])
    elif lista[i] % 2 != 0:
        impar.append(lista[i])
    i += 1
        
print (f'Lista completa: {lista}\nLista de valores pares: {par}\nLista de valores ímpares: {impar}\n')

#Exercício 3:

print('\nExercício 3)\n\n')

list1, list2, listfinal = [], [], []
import random
for i in range (10):
    list1.append(random.randint(1,100))
    list2.append(random.randint(1,100))
for j in range (10):
    listfinal.append(list1[j])
    listfinal.append(list2[j])

print(f'Primeira lista aleatória: {list1}\nSegunda lista aleatória: {list2}\nLista intercalada: {listfinal}\n')

print (f'\nExercício 4)\n\n')

import re
newlist = []
lista = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'.lower().split()
for i in range (len(lista)):
    lista[i] = re.sub ('[,.:]', '', lista[i])
    if lista[i].endswith('p' or 'y' or 't' or 'h' or 'o' or 'n') or lista[i].startswith('p' or 'y' or 't' or 'h' or 'o' or 'n'):
        newlist.append(lista[i])
    '''elif lista[i].endswith('y') or lista[i].startswith('y'):
        newlist.append(lista[i])
    elif lista[i].endswith('t') or lista[i].startswith('t'):
        newlist.append(lista[i])
    elif lista[i].endswith('h') or lista[i].startswith('h'):
        newlist.append(lista[i])
    elif lista[i].endswith('o') or lista[i].startswith('o'):
        newlist.append(lista[i])
    elif lista[i].endswith('n') or lista[i].startswith('n'):
        newlist.append(lista[i])
    '''
print (f'A lista principal é a seguinte: \n{lista}\n\nA lista contendo as palavras iniciando ou terminando com "Python":\n{newlist}\n')

#Exercício 5:

print(f'\nExercício 5)\n\n')


import re
j, flist = 0, []
lista = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'.lower().split()
for i in range (len(lista)):
    lista[i] = re.sub ('[,.:]', '', lista[i])

    if len(lista[i]) > 4 and ('p' in lista [i] or 'y' in lista[i] or 't' in lista [i] or 'h' in lista[i] or 'o' in lista [i] or 'n' in lista[i]):
        j += 1
        flist.append(lista[i])
print (f'Existem {j} palavras contendo as letras "Pyhton", como pode ser visto abaixo:\n\n{flist}')

    
