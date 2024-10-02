# 1. Dada uma lista, retornar o elemento que está
# à cabeça (ou seja, na posição 0).
def head_element(lst):
    return lst[0]

# 2. Dada uma lista, retornar a sua cauda (ou seja,
# todos os elementos à exceção do primeiro).
def get_tail(lst):
    tail = []
    for i in lst[1:]:       # lst[1:] obter todos os elementos a partir do índice 1 até o final
        tail.append(i)      # lst[start:end:step]
    return tail

# 3. Dado um par de listas com igual comprimento,
# produzir uma lista dos pares dos elementos homólogos
def homologous_list(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        result.append((lst1[i], lst2[i]))
    return result

# 4. Dada uma lista de números, retorna o menor elemento.
def lowest_element(lst):
    for i in range(1, len(lst)):
       if lst[i] < lst[0]:      # lst[0] vai armazenar o menor valor
           lst[0] = lst[i]
    return lst[0]

# 5. Dada uma lista de números, retorna um par formado pelo menor elemento
# e pela lista dos restantes elementos.
def pair_lowest_list(lst):
    min_value = min(lst)
    new_lst = lst.copy()
    new_lst.remove(min_value)
    return min_value, new_lst

# 6. Dada uma lista de números, calcular o máximo e o mínimo,
# retornando-os num tuplo
def max_min(lst):
    result = []
    max_value = max(lst)
    min_value = min(lst)
    result.append((max_value, min_value))
    return result

# 7. Dada uma lista de números, retorna um triplo formado pelos
# dois menores elementos e pela lista dos restantes elementos.
def min_min_list(lst):
    min1 = float('inf')
    min2 = float('inf')
    for number in lst:
        if number < min1:
            min2 = min1     # atualiza o segundo menor
            min1 = number   # atualiza o menor
        elif number < min2 and number != min1:  # caso number seja menor que min2
            min2 = number                       # e diferente de min1
    new_lst = [x for x in lst if x != min1 and x != min2]
    return min1, min2, new_lst

'''
    min_value = min(lst)
    lst.remove(min_value)
    second_min_value = min(lst)
    lst.remove(second_min_value)
    return min_value, second_min_value, lst
'''

# 8. Dada uma lista ordenada de números, calcular se possível a respectiva
# média e mediana, retornando-as num tuplo.
def mean_median(lst):
    soma = 0
    count = len(lst)
    median = 0
    lst.sort()
    for number in lst:
        soma += number
        if count % 2 == 0:
            mid_index = count // 2 - 1      # representa o primeiro elemento do meio.
            mid_index2 = count // 2         #  representa o segundo elemento do meio.
            median =  (lst[mid_index] + lst[mid_index2]) / 2 # média dos 2 elementos
        elif count % 2 != 0:
            mid_index = count // 2        # count//2, arredona o numero
            median = lst[mid_index]
    return soma/count, median

numbers = [1, 10, 100, 1000]
numbers2 = [1, 0.1, 0.01, 0.001]
numbers3 = [8, 6, 10, 7, 11, 9]

print("1. " + str(head_element(numbers)))
print("2. " + str(get_tail(numbers)))
print("3. " + str(homologous_list(numbers, numbers2)))
print("4. " + str(lowest_element(numbers)))
print("5. " + str(pair_lowest_list(numbers3)))
print("6. " + str(max_min(numbers2)))
print("7. " + str(min_min_list(numbers3)))
print("8. " + str(mean_median(numbers3)))
