# Найти среднее число или число как можно ближе стоящее к средине, в заданом диапазоне простых чиселю
# list_nums = [5, 7, 10, 13, 17]
# В данном случае это число 11, но посколько его нет ближе всего к нему стоит 10.

import math

def average(x, y):
    list_nums = []

    for nums in range(x, y):
        if all(nums % i != 0 for i in range(2, int(math.sqrt(nums)) + 1)):
            list_nums.append(nums)

    avg = sum(list_nums) / len(list_nums)
    mean = min(list_nums, key=lambda num: abs(num - avg))

    print(mean)

average(10, 100020)

# Даный скрипт для поиска простых чисел можно еще ускорить, использовав Решето Ератосфена


# Если в списке не четное количество элементов? найти число которое находится по средине
# если четное количество элементов находим среднее между двумя четными числами

def median(lst):
    lst = sorted(lst)

    if len(lst) % 2 == 0:
        even = (lst[int(len(lst) / 2)] + lst[int(len(lst) / 2) - 1]) / 2.0
        return even

    else:
        uneven = lst[int(len(lst) / 2)]
        return uneven

median([1, 7, 3, 6, 8])
