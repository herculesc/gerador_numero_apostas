"""Gerador de número de aposta, para esse problema como entrada o apostador irá
passar a quantidade de aposta o código deve retornar os números de apostas
possuir 5 dígitos e
não deve ser repetido
de 01 a 60"""

import random

quant = int(input("Quantos Jogos: "))
num_aposta = {}

'''Função que gera valores aleatores'''
def gerador_numero():
    """"Função que gera valor aleatorio de 1 a 60"""
    random_num = ((random.randrange(1, 60, 1)))
    return random_num

'''Remover valor repetidos da lista'''
def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

'''Função que gera uma lista com 5 valores aleatores'''
def gerador_de5_aposta():
    vect_num_apost = [] # Vector para guardar os numero de aposta

    # Cria primeiro valor da lista
    numero = (gerador_numero())
    vect_num_apost.append(numero)

    # Enquanto a lista for meno que 5
    while len(vect_num_apost) < 5:
        #Gera numero
        numero = (gerador_numero())
        vect_num_apost.append(numero)

        #removendo valor repetido da lista
        vect_num_apost = remove_repetidos(vect_num_apost)
    # ordenar em ordem cresente
    valor_ordenado = sorted(vect_num_apost)
    return valor_ordenado



'''Criar dicionario com os 5 numeros usando o id da repetição quant'''
def criar_dicionario_aposta(quant):
    for id in range(quant):
        new_num_apost = gerador_de5_aposta()
        if id == 0:
            # Cria dicionario
            num_aposta = {id + 1: new_num_apost}
        else:
            # Atribui valor ao dicionario
            num_aposta[id + 1] = new_num_apost
        # Retorna o
    return num_aposta

# Cria dicionario com as apostas
num_aposta = criar_dicionario_aposta(quant)


# Imprime os valores
for i in num_aposta:
    num_aposta[i]
    print(num_aposta[i])
    #print(num_aposta.keys())