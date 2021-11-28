import time
import random
from merge_sort import merge_sort
from quick_sort import quick_sort
from radix_sort import radix_sort
from insertion_sort import insertion_sort

def performance(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__} runtime - {end - start:0.8f}')
        return result
    return wrapper

merge_sort = performance(merge_sort)
quick_sort = performance(quick_sort)
radix_sort = performance(radix_sort)
insertion_sort = performance(insertion_sort)

A = [random.randint(10000, 99999) for i in range(100000)]

merge_sort(A)
quick_sort(A)
radix_sort(A)
insertion_sort(A)