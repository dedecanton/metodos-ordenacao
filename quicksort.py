# Implementação para ordenar uma lista de números em ordem crescente ou decrescente (alterar no retorno conforme os comentários)
def quicksort(lista):
    tamanho = len(lista)

    if (tamanho <= 1):
        return lista

    pivo = lista.pop()  # por padrão vamos definir o pivo como o último elemento da lista

    # vamos criar dois arrays para os números maiores e menores que o pivô
    menores = []
    maiores = []

    for numero in lista:
        if (numero <= pivo):
            menores.append(numero)
        else:
            maiores.append(numero)

    # recursividade para realizar o algoritimo nos arrays "sub-problemas" que vão ser criados até chegar à solução final

    # para ordenar em ordem crescente:
    return quicksort(menores) + [pivo] + quicksort(maiores)

    # para ordenar em ordem decrescente:
    # return quicksort(maiores) + [pivo] + quicksort(menores)


# ******************* TESTES *************

# listas
lista1 = [1, 50, 562, 402, 6, 4856, 4, 564, 65, 231, 3, 56, 897, 9, 31232, 1, 54168, 4, 8969, 1, 50, 562, 402, 6, 4856, 4, 564, 65, 231, 3, 56, 897, 9, 31232, 1, 54168, 4, 8969, 1, 50, 562, 402, 6, 4856, 4, 564, 65, 231, 3, 56, 897, 9, 31232, 1, 54168, 4,
          8969, 1, 50, 562, 402, 6, 4856, 4, 564, 65, 231, 3, 56, 897, 9, 31232, 1, 54168, 4, 8969, 1, 50, 562, 402, 6, 4856, 4, 564, 65, 231, 3, 56, 897, 9, 31232, 1, 54168, 4, 8969, 1, 50, 562, 402, 6, 4856, 4, 564, 65, 231, 3, 56, 897, 9, 31232, 1, 54168, 4, 8969]
lista2 = [5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 9, 9, 9, 9,
          9, 9, 6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3]
lista3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
lista4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lista5 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


print(quicksort(lista1))
print(quicksort(lista2))
print(quicksort(lista3))
print(quicksort(lista4))
print(quicksort(lista5))