from operator import truediv


# 1. Dada uma lista, retorna o seu comprimento
def comprimento(lst):
    if not lst:
        return 0
    return 1 + comprimento(lst[1:])

# 2. Dada uma lista de números, retorna a respetiva soma.
def soma(lst):
    if not lst:
        return 0
    return lst[0] + soma(lst[1:])

#3. Dada uma lista e um elemento, verifica se o elemento
# ocorre na lista. Retorna um valor booleano.
def existe(color, colors):
    if not colors:
        return False
    if colors[0] == color:
        return True
    return existe(colors[1:])

# 4. Dadas duas listas, retorna a sua concatenação.
def concat(lst1, lst2):
    if not lst1:
        return lst2
    return [lst1[0]] + concat(lst1[1:], lst2)

# 5. Dada uma lista, retorna a sua inversa.
def inverte(lst):
    if not lst:
        return []
    return [lst[-1]] + inverte(lst[:-1])

# 6. Dada uma lista, verifica se forma uma capicua, ou seja,
# se, quer se leia da esquerda para a direita ou vice-versa,
# se obtêmm a mesma sequência de elementos.
def capicua(lst):
    if len(lst) <= 1:
        return True
    if lst[0] == lst[-1]:
        return capicua(lst[1:-1])
    else:
        return False

# 7. Dada uma lista de listas, retorna a concatenação dessas listas.
def concat_listas(lst1, lst2):
    if not lst1:
        return lst2
    return [lst1[0]] +  concat_listas(lst1[1:], lst2)

# 8. Dada uma lista, um elemento x e outro elemento y, retorna uma
# lista similar à lista de entrada, na qual x é substituido por y
# em todas as ocorrências de x.
def substitui(x, y, lst):
    if not lst:
        return []
    if lst[0] == x:
        return [y] + substitui(x, y, lst[1:])
    else:
        return [lst[0]] + substitui(x, y, lst[1:])



# 9. Dadas duas listas ordenadas de números, calcular a união
# ordenada mantendo eventuais repetições.
def fusao_ordenada(lst1, lst2):
    if not lst1:
        return lst2
    if not lst2:
        return lst1
    if lst1[0] <= lst2[0]:
        return [lst1[0]] + fusao_ordenada(lst1[1:], lst2)
    if lst2[0] <= lst1[0]:
        return [lst2[0]] + fusao_ordenada(lst1, lst2[1:])

# 10. Dado um conjunto, na forma de uma lista, retorna uma lista
# de listas que representa o conjunto de todos os subconjuntos
# do conjunto dado.
def generate_subsets(original_set):
    if not original_set:
        return [[]]
    first_element = original_set[0]
    subsets_without_first = generate_subsets(original_set[1:])
    subsets_with_first = [[first_element] + subset for subset in subsets_without_first]
    return subsets_without_first + subsets_with_first


colors = ["Green", "Red", "Blue", "Yellow", "Purple"]
numbers = [2, 5, 9, 15, 22]
more_numbers = [3, 5, 10, 22]
set = [1, 2, 3]
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
bob = [
    ["b", "o", "b"],
    ["o", "b", "o"],
    ["b", "o", "b"],
]

print("1. " + str(comprimento(colors)))
print("2. " + str(soma(numbers)))
print("3. " + str(existe("Green", colors)))
print("4. " + str(concat(colors, numbers)))
print("5. " + str(inverte(colors)))
print("6. " + str(capicua(numbers)))
print("7. " + str(concat_listas(matriz, bob)))
print("8. " + str(substitui("Red", "Green", colors)))
print("9. " + str(fusao_ordenada(numbers, more_numbers)))
print("10. " + str(generate_subsets(set)))
