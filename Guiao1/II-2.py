# 1. Dada uma lista de pares, produzir um par com as listas dos
# primeiros e segundos elementos desses pares.
# separar ([( a1, b1), ... (an, bn)]) = ([a1, ... an], [b1, ... bn])
def separar(lst):
    if not lst:
        return [], []
    x, y = separar(lst[1:])
    return [lst[0][0]] + x, [lst[0][1]] + y


# 2. Dada uma lista l e um elemento x, retorna um par formado pela
# lista dos elementos de l diferentes de x e pelo número de
# ocorrências x em l.
# Exemplo:
#>>> remove_e_conta( [ 1 , 6 , 2 , 5 , 5 , 2 , 5 , 2 ] , 2 ) ( [ 1 , 6 , 5 , 5 , 5 ] , 3 )
def remove_and_count(lst, num):
    if num not in lst:
        return 0
    lst.remove(num)
    return 1 + remove_and_count(lst, num)

# 3. Dada uma lista, retorna o número de ocorrências de cada
# elemento, na forma de uma lista de pares (elemento,contagem).
def  count_occurrences_recursive(lst, occurrences=None):
    if occurrences is None:  # Inicializar o dicionário na primeira chamada
        occurrences = {}

    if not lst:  # Caso base: se a lista está vazia, retorna as ocorrências
        return occurrences

        # Contar a ocorrência do primeiro elemento
    if lst[0] in occurrences:
        occurrences[lst[0]] += 1
    else:
        occurrences[lst[0]] = 1

    return count_occurrences_recursive(lst[1:], occurrences)

def occurrences_to_list(occurrences):
    return [(key, value) for key, value in occurrences.items()]



numbers = [1, 6, 2, 5, 5, 2, 5, 2]
pairs = [(1, "a"), (2, "b"), (3, "c")]

print("1. " + str(separar(pairs)))
occurrences_dict = count_occurrences_recursive(numbers)
occurrences_list = occurrences_to_list(occurrences_dict)
print("3. " + str(occurrences_list))
count = remove_and_count(numbers, 2)
print("2. " + str(numbers),str(count))
