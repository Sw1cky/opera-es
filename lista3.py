import random
from collections import Counter


lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = list(set(lista1) & set(lista2))
interseccao.sort()

repet_lista1 = Counter(lista1)
repet_lista2 = Counter(lista2)


print("Primeira lista: -", lista1)
print("Segunda lista: -", lista2)
print("Interseccao dass listas -", interseccao)

print("Contagem de repetições entre as listas")
for elemento in interseccao:
    print(f"{elemento}: (lista1={repet_lista1[elemento]}, lista2={repet_lista2[elemento]})")