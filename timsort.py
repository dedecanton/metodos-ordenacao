MINIMUM = 32

def find_minrun(array_length):
    r = 0
    while array_length >= MINIMUM:
        r |= array_length & 1
        array_length >>= 1
    return array_length + r

def insertion_sort(array, start, end):
    # insertion sort no run específico  que está sendo ordenado
    for index in range(start+1, end+1):
        current_element = array[index]
        prev_index = index-1
        # realizar troca enquanto (o elemento atual for menor que o anterior) e (o current_element não estiver no primeiro indice do run, ou seja, ainda tem elemento anterior a ser comparado)
        while current_element < array[prev_index] and prev_index >= start:
            array[prev_index+1] = array[prev_index]
            prev_index -= 1
        array[prev_index+1] = current_element
    return array


def merge(array, start_index, middle_index, end_index):

    left_length = middle_index - start_index + 1
    right_length = end_index - middle_index

    # primeiro array a ser comparado -> início do run até elemento do meio (incluindo ele)
    left = array[start_index:middle_index + 1]
    # segundo array a ser comparado -> elemento do meio (não incluindo ele) até o fim do run
    right = array[middle_index + 1:end_index + 1]

    # indices para comparação entre os arrays
    index_left, index_right = 0, 0

    current_index = start_index

    # enquanto tiver elementos a ser comparado em ambos os arrays
    while index_right < right_length and index_left < left_length:
        if left[index_left] <= right[index_right]:
            array[current_index] = left[index_left]
            index_left += 1
        else:
            array[current_index] = right[index_right]
            index_right += 1

        current_index += 1

    # enquanto tiver elementos a ser comparado apenas no array "left"
    while index_left < left_length:
        array[current_index] = left[index_left]
        current_index += 1
        index_left += 1

    # enquanto tiver elementos a ser comparado apenas no array "right"
    while index_right < right_length:
        array[current_index] = right[index_right]
        current_index += 1
        index_right += 1


def timsort(array):
    array_length = len(array)
    minrun = find_minrun(array_length)

    # iteração no array em um intervalo do valor do minrun
    for start in range(0, array_length, minrun):
        end = min(start + minrun - 1, array_length - 1)
        insertion_sort(array, start, end)

    size = minrun
    while size < array_length:

        for left in range(0, array_length, 2 * size):

            mid = min(array_length - 1, left + size - 1)
            right = min((left + 2 * size - 1), (array_length - 1))
            merge(array, left, mid, right)

        size = 2 * size


# ******************* TESTES *************

# listas
lista1 = [1, 50, 562, 402, 6, 4856, 4, 564, 65, 231, 3, 56, 897, 9, 31232, 1, 54168, 4, 8969, 1, 50, 562, 402, 6, 4856, 4, 564, 65, 231, 3, 56, 897, 9, 31232, 1, 54168, 4, 8969, 1, 50, 562, 402, 6, 4856, 4, 564, 65, 231, 3, 56, 897, 9, 31232, 1, 54168, 4,
          8969, 1, 50, 562, 402, 6, 4856, 4, 564, 65, 231, 3, 56, 897, 9, 31232, 1, 54168, 4, 8969, 1, 50, 562, 402, 6, 4856, 4, 564, 65, 231, 3, 56, 897, 9, 31232, 1, 54168, 4, 8969, 1, 50, 562, 402, 6, 4856, 4, 564, 65, 231, 3, 56, 897, 9, 31232, 1, 54168, 4, 8969]
lista2 = [5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 9, 9, 9, 9,
          9, 9, 6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3]
lista3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
lista4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lista5 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


timsort(lista1)
print(lista1)
print('-----------------------')

timsort(lista2)
print(lista2)
print('-----------------------')

timsort(lista3)
print(lista3)
print('-----------------------')

timsort(lista4)
print(lista4)
print('-----------------------')

timsort(lista5)
print(lista5)
print('-----------------------')
