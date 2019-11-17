#Autor:Walber Conceição de Jesus Rocha

def bf(pa, po):
    po_aux = []
    pa_aux = []
    pa_aux2 = pa.copy()
    for processo in po:
        pa_atualizada = pa_aux2.copy()
        pa_atualizada.sort()
        indice_p = po.index(processo)
        for espaco in pa_atualizada:
            if(processo <= espaco):
                indice_esp = pa.index(espaco)
                indice_esp2 = pa_aux2.index(espaco)
                novo_espaco = espaco - processo
                pa_aux.append((str(indice_p)+
                            "\t"+str(processo)+
                            "\t"+str(indice_esp)+
                            "\t"+str(espaco)+
                            "\t"+str(novo_espaco)))
                po_aux.append(po[indice_p])
                del(pa_aux2[indice_esp2])
                break
            else:
                continue

    print("No. do processo | Tamanho do processo | No partição | Tamanho da partição | Sobra")
    for espaco in pa_aux:
        print(espaco)

    print("Processos em espera:")
    espera = list(set(po) - set(po_aux))
    for processo in espera:
        indice_p = po.index(processo)
        print("--------------------")
        print("No. Processo: "+str(indice_p)+"\nTamanho do processo: "+str(processo))

def ff(pa, po):
    po_aux = []
    pa_aux = []
    pa_aux2 = pa.copy()
    for processo in po:
        indice_p = po.index(processo)
        pa_atualizada = pa_aux2.copy()
        for espaco in pa_atualizada:
            if(processo <= espaco):
                indice_esp = pa.index(espaco)
                indice_esp2 = pa_aux2.index(espaco)
                novo_espaco = espaco - processo
                pa_aux.append((str(indice_p)+
                            "\t"+str(processo)+
                            "\t"+str(indice_esp)+
                            "\t"+str(espaco)+
                            "\t"+str(novo_espaco)))
                po_aux.append(po[indice_p])
                del(pa_aux2[indice_esp2])
                break
            else:
                continue
    
    print("No. do processo | Tamanho do processo | No partição | Tamanho da partição | Sobra")
    for espaco in pa_aux:
        print(espaco)

    print("Processos em espera:")
    espera = list(set(po) - set(po_aux))
    for processo in espera:
        indice_p = po.index(processo)
        print("--------------------")
        print("No. Processo: "+str(indice_p)+"\nTamanho do processo: "+str(processo))

def wf(pa, po):
    po_aux = []
    pa_aux = []
    pa_aux2 = pa.copy()
    for processo in po:
        pa_atualizada = pa_aux2.copy()
        pa_atualizada.sort(reverse=True)
        indice_p = po.index(processo)
        for espaco in pa_atualizada:
            if(processo <= espaco):
                indice_esp = pa.index(espaco)
                indice_esp2 = pa_aux2.index(espaco)
                novo_espaco = espaco - processo
                pa_aux.append((str(indice_p)+
                            "\t"+str(processo)+
                            "\t"+str(indice_esp)+
                            "\t"+str(espaco)+
                            "\t"+str(novo_espaco)))
                po_aux.append(po[indice_p])
                del(pa_aux2[indice_esp2])
                break
            else:
                continue
    
    print("No. do processo | Tamanho do processo | No partição | Tamanho da partição | Sobra")
    for espaco in pa_aux:
        print(espaco)

    print("Processos em espera:")
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