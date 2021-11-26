import time
import random

def performance(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func} runtime - {end - start:0.8f}')
        return result
    return wrapper


@performance
def merge(array_1, array_2):
    index_1 = 0
    index_2 = 0
    merged_array = []
    while len(array_1) > index_1 and len(array_2) > index_2:
        if array_1[index_1] > array_2[index_2]:
            merged_array.append(array_2[index_2])
            index_2 += 1
        else:
            merged_array.append(array_1[index_1])
            index_1 += 1

    return merged_array + array_1[index_1:] + array_2[index_2:]

@performance
def merge3(array_1, array_2):
    return sorted(array_1 + array_2)

@performance
def merge4(array_1, array_2):
    result = []
    while array_1 and array_2:
        if array_1[0] > array_2[0]:
            result.append(array_2.pop())
        else:
            result.append(array_1.pop())
    return result + array_1 + array_2 



A = [random.randint(0, 100000) for i in range(100000)]
B = [random.randint(0, 100000) for i in range(1000000)]
print('lists created')
from heapq import merge as merge2

merge2 = performance(merge2)

merge(A, B)
merge2(A, B)
merge3(A, B)
merge4(A, B)