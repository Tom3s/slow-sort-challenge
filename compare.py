from bigO import BigO
from bigO import algorithm

from slow_sort import slow_sort as slow_sort_algorithm
from bubble_sort import bubble_sort

numbers = []

with open('numbers10000.txt', 'r') as file:
    for line in file:
        numbers.append(int(line))

lib = BigO()

lib.compare(slow_sort_algorithm, bubble_sort, numbers, 10)
