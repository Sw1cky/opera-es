def combinar_mescla(lista1, lista2):
    mescla_lista = []
  
    tamanho_lista1 = len(lista1)
    tamanho_lista2 = len(lista2)

    for i in range(min(tamanho_lista1, tamanho_lista2)):
        mescla_lista.append(lista1[i])
        mescla_lista.append(lista2[i])
   
    if tamanho_lista1 > tamanho_lista2:
        mescla_lista.extend(lista1[tamanho_lista2:])
    else:
        mescla_lista.extend(lista2[tamanho_lista1:])
    return mescla_lista

def receber_lista(nome_lista):
    quantidade = int(input(f"Digite a quantidade de elementos da {nome_lista}: "))
    lista = []
    print(f"Digite os {quantidade} elementos da {nome_lista}:")
    for _ in range(quantidade):
        elemento = int(input())
        lista.append(elemento)
    return lista
lista1 = receber_lista("lista 1")
lista2 = receber_lista("lista 2")


mescla_lista = combinar_mescla(lista1, lista2)
print("Mistura das listas:", " ".join(map(str, mescla_lista)))
