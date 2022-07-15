"""Gerador de número de aposta, para esse problema como entrada o apostador irá
passar a quantidade de aposta o código deve retornar os números de apostas
possuir 5 dígitos e
não deve ser repetido
de 01 a 60"""

import random

# Quantidade de Jogo
quant = int(input("Quantos Jogos: "))

num_aposta = {}

'''
# Gera 5 digítos aleatórios de 1 e 60
-> Enquanto valor < 5:
     cria um  número aleatório e adiciona a lista valor e atribui +1 ao contador
     
-> Se o valor cont for o segundo valor:
    gero um número randômico e caso esse numero seja diferir ao anterior é adicionado a lista
    a função retorna os valores em ordem crescente
'''
def gera_numero():
    valor = []
    cont = 1
    while len(valor) < 5:
        if cont == 1 :
            numero = ((random.randrange(1, 60, 1)))
            valor.append(numero)
            cont +=1
        #print(f'contador: {cont}')
        if cont > 1:
            numero = ((random.randrange(1, 60, 1)))
            print(f'contador: {cont}')

            if valor[cont-2] != numero:
                print(valor[cont-2])
                valor.append(numero)

    valor_ordenado = sorted(valor)
    return valor_ordenado


# Criar dicionario com os 5 numeros usando o id da repetição quant
for id in range(quant):
    new_numero = gera_numero()
    if id == 0:
        num_aposta = {id+1: new_numero}
    else:
        num_aposta[id + 1] = new_numero

# Imprime os valores
for i in num_aposta:
    num_aposta[i]
    print(num_aposta[i])
    #print(num_aposta.keys())