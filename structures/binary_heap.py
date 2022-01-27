heap = []


def check_boundries(heap, index):
    return 0 <= index < len(heap)


def get_parent(heap, index):
    if index == 0:
        return 0

    if not check_boundries(heap, index):
        raise IndexError

    return (index - 1) // 2


def switch(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]


def get_children_indices(parent_index):
    return ((parent_index * 2) + 1, (parent_index * 2) + 2)


def get_proper_child(heap, parent_index):
    left, right = get_children_indices(parent_index)
    left_exists = check_boundries(heap, left)
    right_exists = check_boundries(heap, right)

    if left_exists and right_exists:
        if heap[left] > heap[right]:
            return right
        else:
            return left

    if left_exists:
        return left

    if right_exists:
        return right

    return -1


def bubble_down(heap):
    parent = 0

    while True:
        if (child := get_proper_child(heap, parent)) >= 0:
            if heap[parent] > heap[child]:
                switch(heap, parent, child)
                parent = child
                continue
        break


def bubble_up(heap):
    target_index = len(heap) - 1
    parent_index = get_parent(heap, target_index)

    while heap[parent_index] > heap[target_index]:
        switch(heap, parent_index, target_index)
        target_index = parent_index
        parent_index = get_parent(heap, target_index)


def insert(heap, value):
    heap.append(value)
    bubble_up(heap)


def extract(heap):
    switch(heap, 0, -1)
    to_extract = heap.pop()
    bubble_down(heap)
    return to_extract
