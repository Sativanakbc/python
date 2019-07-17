def emprestimo():
    #
    # O cliente não pode ser menor que 25 anos ou maior que 60 anos
    # Salarios menores que 2500 não podem solicitar empréstimo maior que 6000
    # Salários menos que 1000 não podem solicitar empréstimo
    #

    nome = str(input('Digite o seu nome:'))
    idade = int(input('Informe sua idade:'))
    if(idade < 25 or idade > 60):
        print('Infelizmente você não pode realizar empréstimos.')
    else:
        salario = int(input('Quanto você ganha atualmente?'))
        if(salario < 1000):
            print('Infelizmente você não pode realizar empréstimos.')
        else:
            valorEmprestimo = int(input('Qual o valor que deseja para empréstimo?'))
            if(salario < 2500 and valorEmprestimo > 6000):
                print('Infelizmente você não pode realizar empréstimos.')
            else:
                print(nome + " seu empréstimo no valor de " + str(valorEmprestimo)+ " foi efetivado.")
                
#############################################################################################################

def escadinha():
    material = str(input('Qual o material da sua escada?'))
    degraus = int(input('Quantos degraus você deseja?'))
    escada = ''

    for degrau in range(0, degraus):
        escada += material
        print(escada)
        
#############################################################################################################

def embaralhador(lista):
    import math
    import random as ran
    valor_temp = None
    indice_aleat = None

    for i in range(len(lista) - 1, 0, -1):
        indice_aleat = ran.randint(0, len(lista) - 1)
        valor_temp = lista[i]
        lista[i] = lista[indice_aleat]
        lista[indice_aleat] = valor_temp
    
    print(lista)
    
#############################################################################################################

def definePares(garotas, garotos):
    for a in garotas:
        print('')
        for b in garotos:
            print(b + ' par de ' + a)

#definePares(['Ana', 'Bia', 'Beatriz'], ['Rafael', 'Leo', 'Hugo'])

#############################################################################################################

def defineParesIndependente(garotas, garotos):
    participantes = garotas + garotos
    participantes.sort()
    for a in participantes:
        for b in participantes:
            if(b == a):
                pass
            else:
                print(b + ' par de ' + a)
            

#defineParesIndependente(['Ana', 'Bia'], ['Rafael', 'Leo'])

#############################################################################################################

def verificaLista(lista):
    for indice in lista:
        if indice == 1:
            pass
        elif indice != indice - 1:
            return print(False)
    return print(True)

verificaLista([1,1,1,1])