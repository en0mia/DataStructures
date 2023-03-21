# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 21/03/23


def get_parent_index(index: int) -> int:
    return int((index - 1) / 2)


def get_left_child_index(index: int) -> int:
    return 2 * index + 1


def get_right_child_index(index: int) -> int:
    return 2 * index + 2


def heapify(heap: list, starting_index: int) -> None:
    if len(heap) == 0:
        return

    if get_left_child_index(starting_index) < len(heap):
        left_child_index = get_left_child_index(starting_index)
        right_child_index = get_right_child_index(starting_index)
        if heap[starting_index] > heap[left_child_index] or \
                (right_child_index < len(heap) and heap[starting_index] > heap[right_child_index]):
            if heap[left_child_index] < heap[right_child_index]:
                # Swap
                heap[left_child_index], heap[starting_index] = heap[starting_index], heap[left_child_index]
                heapify(heap, left_child_index)
            elif right_child_index < len(heap):
                # Swap
                heap[right_child_index], heap[starting_index] = heap[starting_index], heap[right_child_index]
                heapify(heap, right_child_index)


def insert(heap: list, element) -> None:
    heap.append(element)

    if len(heap) == 1:
        return

    element_index = len(heap) - 1

    while heap[get_parent_index(element_index)] > heap[element_index]:
        parent_index = get_parent_index(element_index)
        parent = heap[parent_index]
        heap[parent_index] = heap[element_index]
        heap[element_index] = parent
        element_index = parent_index


def extract_min(heap: list):
    if len(heap) == 0:
        return None
    min_value = heap[0]
    heap[0] = heap[-1]
    del heap[-1]

    heapify(heap, 0)
    return min_value
