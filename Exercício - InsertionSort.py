import random

def insertionsort(array):
    for i in range(1, len(array)):
        v = array[i]
        j = i - 1

        while (j >= 0) and (v < array[j]):
            array[j + 1] = array[j]
            j = (j -1)
            array[j + 1] = v

lista = []
for i in range(0, 30):
    lista.append(random.randint(1, 500))
    if lista[i] %2 == 1:
        lista[i] = lista[i]
    else:
        lista[i] = lista[i] + 1

print("\nLista :\n",lista)
insertionsort(lista)
print('\nLista em ordem crescente:\n',lista)