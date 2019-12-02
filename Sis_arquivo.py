#Discente: Walber Conceicao de Jesus Rocha
#Matricula: 2019129450

import math

tam_bloco = float(input("Defina o tamanho que cada bloco terá: "))
num_particoes = input ("Defina o numero de particoes: ")
particoes = []
for i in range(0, int(num_particoes)):
    particoes.append(-1)

while(True):
    count = 0
    print("-------------")
    bloco_inicial = int(input("Informe a posicao inicial do arquivo: "))
    nome_arquivo = input("Informe o nome do arquivo: ")
    arquivo = int(input("Informe o tamanho do arquivo: "))
    qtd_blocos = math.ceil(arquivo/tam_bloco)
    try:
        for i in range(bloco_inicial, (qtd_blocos+bloco_inicial)):
            if(particoes[i] == -1):
                count += 1
            else:
                count = 0
        if(count >= qtd_blocos):
            for i in range(bloco_inicial-1, (qtd_blocos+bloco_inicial)):
                particoes[i] = nome_arquivo
        else:
            print("Memoria cheia!!")
    except:
        print("Nao e possivel alocar na posicao indicada, indique uma nova posicao") 
    print(particoes)



