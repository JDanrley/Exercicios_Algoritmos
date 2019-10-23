#Questão A:
print ('Exercício A - Valor resultante do pseudocódigo.\n')
x, y = 2, 5
if y > 8:
    y *= 2
else:
    x *= 2
print (f'Resultado: {x + y}')

#Questão B:

print ('\nExercício B - Vezes em que o pseudocódigo exibiria a palavra "Oi"\n')
       
cont = 0
for i in range (1, 10):
    if i != 3:
        for j in range (1, 7):
            cont += 1 #Simulando o print(cont)
       
print (f'Resultado: {cont} vezes.')

#Questão C:

print (f'\nQuestão C - Números pares e divisíveis por 7 no range 1067 e 3627.\n')
cont = 0
for i in range (1067, 3628):
    if i % 7 == 0 and i % 2 == 0:
        cont += 1
print (f'Resultado: {cont}.\n')

#Questão D:

print (f'Questão D - Números sortudos da Daniela.\n')

cont = 0
for i in range (18644, 33088):
    j = str(i)
    if j.count('7') == 0 and j.count('2') != 0:
        cont += 1
print (f'Resultado: {cont}\n')

#Questão E:

print (f'Números de telefone aceitos.\n')
lista = '''213752 216732 221063 221545 225583 229133 230648 233222
236043 237330 239636 240138 242123 246224 249183 252936
254711 257200 257607 261424 263814 266794 268649 273050
275001 277606 278997 283331 287104 287953 289137 291591
292559 292946 295180 295566 297529 300400 304707 306931
310638 313595 318449 319021 322082 323796 326266 326880
327249 329914 334392 334575 336723 336734 338808 343269
346040 350113 353631 357154 361633 361891 364889 365746
365749 366426 369156 369444 369689 372896 374983 375223
379163 380712 385640 386777 388599 389450 390178 392943
394742 395921 398644 398832 401149 402219 405364 408088
412901 417683 422267 424767 426613 430474 433910 435054
440052 444630 447852 449116 453865 457631 461750 462985
463328 466458 469601 473108 476773 477956 481991 482422
486195 488359 489209 489388 491928 496569 496964 497901
500877 502386 502715 507617 512526 512827 513796 518232
521455 524277 528496 529345 531231 531766 535067 535183
536593 537360 539055 540582 543708 547492 550779 551595
556493 558807 559102 562050 564962 569677 570945 575447
579937 580112 580680 582458 583012 585395 586244 587393
590483 593112 593894 594293 597525 598184 600455 600953
601523 605761 608618 609198 610141 610536 612636 615233
618314 622752 626345 626632 628889 629457 629643 633673
637656 641136 644176 644973 647617 652218 657143 659902
662224 666265 668010 672480 672695 676868 677125 678315'''.split()

soma, cont, contf, cancelador = 0, 0, 0, 0
for i in lista:
    
    if i[0] != i[5]:            #Comparando o último e primeiro algarismo
        cont += 1               #Variável "cont" amarzena 1 sempre que uma regra é atendida
        
    for j in i:                 #Variável "j" usada para somar todos os itens do nº telefônico
        soma += int(j) 
    if soma % 2 == 0:           #Validando se o número da soma é par
        cont += 1               #Variável "cont" amarzena 1 sempre que uma regra é atendida
    soma = 0
    for k in range (5):         #Ciclo para comparar se os números são iguais uns aos outros, comparando com o seguinte
        if i[k] == i[k + 1]:    #Comparação entre "k" e "k+1", indo apenas até o penúltimo item, sendo apenas 5 repetições
            cancelador += 1     #Flag de identificação se houver repetição
    if cancelador == 0:         
        cont += 1
    cancelador = 0
    if cont == 3:               #Confirmando se as três regras foram atendidas
        contf += 1              #Contador de números que se enquadram
    cont = 0
    
print (f'Resultado: {contf}.')

        
