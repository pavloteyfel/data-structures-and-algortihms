# Binary min Heap implementation

def get_children(root_i, size):
    left = root_i * 2 + 1
    right = root_i * 2 + 2
    # If out of boundary then return -1
    return left if size > left else -1, right if size > right else -1


def get_root(child_i):
    if child_i == 0:
        return 0
    index = (child_i-1) // 2
    return index


def insert(array, value):
    array.append(value)
    child = len(array) - 1
    root = get_root(child)
    while array[root] > array[child]:
        array[root], array[child] = array[child], array[root]
        child = root
        root = get_root(child)


def extract_min(array):
    # swap the root value and the last inserted value
    array[0], array[len(array)-1] = array[len(array)-1], array[0]

    # remove the max value from the array and store it
    max_value = array.pop()

    root = 0

    while True:
        left, right = get_children(root, len(array))

        # If there are no children then stop, base case
        if left < 0 and right < 0:
            break

        # If there are only right
        if left < 0 and right >= 0:
            # then update to left if its bigger
            if array[root] > array[right]:
                array[root], array[right] = array[right], array[root]

                # set the new root
                root = left
            else:
                break

        # If there is only left
        if right < 0 and left >= 0:
            # then update to right if its bigger
            if array[root] > array[left]:
                array[root], array[left] = array[left], array[root]

                # set root to right
                root = right
            else:
                break

        # There are both left and right, then update swap with min
        if right >= 0 and left >= 0:
            if array[right] > array[left]:
                array[left], array[root] = array[root], array[left]

                # set the new root
                root = left

            else:
                array[right], array[root] = array[root], array[right]

                # set the new root
                root = right

    return max_value


array = []

insert(array, 4)
insert(array, 6)
insert(array, 3)
insert(array, 7)
insert(array, 9)
insert(array, 1)
insert(array, 2)
print(array)
extract_min()
print(array)
