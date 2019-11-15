#Autor:Walber Conceição de Jesus Rocha

def bf(pa, po):
    po_aux = []
    pa_aux = pa.copy()
    for processo in po:
        pa_atualizada = pa.copy()
        pa_atualizada.sort()
        indice_p = po.index(processo)
        for espaco in pa_atualizada:
            if(processo <= espaco):
                indice_esp = pa.index(espaco)
                novo_espaco = espaco - processo
                pa[indice_esp] = novo_espaco
                if(type(pa_aux[indice_esp]) == str):
                    swap = pa_aux[indice_esp]
                else:
                    swap = ""
                print(swap)
                pa_aux[indice_esp] = (swap+"\nNo do processo: "+str(indice_p)+
                            "\nTamanho do processo: "+str(processo)+
                            "\nNo partição: "+str(indice_esp)+
                            "\nTamanho da partição: "+str(espaco)+
                            "\nSobra: "+str(novo_espaco))
                po_aux.append(po[indice_p])
                break
            else:
                continue
    
    for espaco in pa_aux:
        print("--------------------")
        print(espaco)

    print("\nProcessos em espera:")
    espera = list(set(po) - set(po_aux))
    for processo in espera:
        indice_p = po.index(processo)
        print("--------------------")
        print("No. Processo: "+str(indice_p)+"\nTamanho do processo: "+str(processo))

def ff(pa, po):
    po_aux = []
    pa_aux = pa.copy()
    for processo in po:
        indice_p = po.index(processo)
        for espaco in pa:
            if(processo <= espaco):
                indice_esp = pa.index(espaco)
                novo_espaco = espaco - processo
                pa[indice_esp] = novo_espaco
                if(type(pa_aux[indice_esp]) == str):
                    swap = pa_aux[indice_esp]
                else:
                    swap = ""
                print(swap)
                pa_aux[indice_esp] = (swap+"\nNo do processo: "+str(indice_p)+
                            "\nTamanho do processo: "+str(processo)+
                            "\nNo partição: "+str(indice_esp)+
                            "\nTamanho da partição: "+str(espaco)+
                            "\nSobra: "+str(novo_espaco))
                po_aux.append(po[indice_p])
                break
            else:
                continue
    
    for espaco in pa_aux:
        print("--------------------")
        print(espaco)

    print("\nProcessos em espera:")
    espera = list(set(po) - set(po_aux))
    for processo in espera:
        indice_p = po.index(processo)
        print("--------------------")
        print("No. Processo: "+str(indice_p)+"\nTamanho do processo: "+str(processo))

def wf(pa, po):
    po_aux = []
    pa_aux = pa.copy()
    for processo in po:
        pa_atualizada = pa.copy()
        pa_atualizada.sort(reverse=True)
        indice_p = po.index(processo)
        for espaco in pa_atualizada:
            if(processo <= espaco):
                indice_esp = pa.index(espaco)
                novo_espaco = espaco - processo
                pa[indice_esp] = novo_espaco
                if(type(pa_aux[indice_esp]) == str):
                    swap = pa_aux[indice_esp]
                else:
                    swap = ""
                print(swap)
                pa_aux[indice_esp] = (swap+"\nNo do processo: "+str(indice_p)+
                            "\nTamanho do processo: "+str(processo)+
                            "\nNo partição: "+str(indice_esp)+
                            "\nTamanho da partição: "+str(espaco)+
                            "\nSobra: "+str(novo_espaco))
                po_aux.append(po[indice_p])
                break
            else:
                continue
    
    for espaco in pa_aux:
        print("--------------------")
        print(espaco)

    print("\nProcessos em espera:")
    espera = list(set(po) - set(po_aux))
    for processo in espera:
        indice_p = po.index(processo)
        print("--------------------")
        print("No. Processo: "+str(indice_p)+"\nTamanho do processo: "+str(processo))

pa = []
po = []

num_part = input ("Defina o numero de particoes: ")
num_proc = input ("Defina o numero de processos: ")

print("Defina o tamanho de cada particao: ")
for i in range(0, int(num_part)):
    tam_part = int(input("Defina o tamanho partição "+ str(i) +": "))
    pa.append(tam_part)

print("Defina o tamanho de cada processo: ")
for i in range(0, int(num_proc)):
    tam_proc = int(input("Defina o tamanho do processo "+ str(i) +": "))
    po.append(tam_proc)

print(" ")
print("1 - FF\n2 - BF\n3 - WF\n4 - Todos")
print("")
met_aloc = input("Metodo de Alocação: ")

if(int(met_aloc) == 1):
    ff(pa, po)
elif(int(met_aloc) == 2):
    bf(pa, po)
elif(int(met_aloc) == 3):
    wf(pa, po)
elif(int(met_aloc) == 4):
    print("\nFIRST FIT")
    ff(pa.copy(),po.copy())
    print("\nBEST FIT")
    bf(pa.copy(),po.copy())
    print("\nWORST FIT")
    wf(pa.copy(),po.copy())
else:
    print("Método selecionado inválido")