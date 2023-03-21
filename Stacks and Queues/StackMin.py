# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 21/03/23


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackMin:
    def __init__(self):
        self.head = None
        self.min_head = None

    def push(self, value: int) -> None:
        node = Node(value)
        min_node = Node(value)
        if self.head:
            node.next = self.head
        else:
            # If this is the first value, it is for sure the minimum
            self.min_head = min_node
        self.head = node

        # If there is a new minimum
        if self.min_head and value < self.min_head.value:
            min_node.next = self.min_head
            self.min_head = min_node

    def pop(self) -> int:
        node = self.head
        self.head = self.head.next

        if node.value == self.min_head.value:
            self.min_head = self.min_head.next

        return node.value

    def get_min(self) -> int:
        if not self.min_head:
            raise Exception("Empty stack!")
        return self.min_head.value
