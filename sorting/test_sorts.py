from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort, merge_sort_v2
from quick_sort import quick_sort
from radix_sort import radix_sort

sample_1_unordered = [23, 4, 32, 65, 7, 12, 87, 93, 35, 65, 83, 21, 5, 9]
sample_1_ordered = [4, 5, 7, 9, 12, 21, 23, 32, 35, 65, 65, 83, 87, 93]

assert bubble_sort(sample_1_unordered) == sample_1_ordered
assert selection_sort(sample_1_unordered) == sample_1_ordered
assert insertion_sort(sample_1_unordered) == sample_1_ordered
assert merge_sort(sample_1_unordered) == sample_1_ordered
assert merge_sort_v2(sample_1_unordered) == sample_1_ordered
assert quick_sort(sample_1_unordered) == sample_1_ordered
assert radix_sort(sample_1_unordered) == sample_1_ordered
