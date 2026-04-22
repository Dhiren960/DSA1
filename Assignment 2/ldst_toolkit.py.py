import ctypes

class DynamicArray:
    def __init__(self, capacity=3):
        self.n = 0
        self.capacity = capacity
        self.A = self._make_array(self.capacity)

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def append(self, x):
        if self.n == self.capacity:
            print(f"[Resize Event] Capacity reached {self.capacity}. Doubling...")
            self._resize(2 * self.capacity)
        self.A[self.n] = x
        self.n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = c

    def pop(self):
        if self.n == 0:
            return None
        element = self.A[self.n - 1]
        self.A[self.n - 1] = None
        self.n -= 1
        return element

    def __str__(self):
        return "[" + ", ".join(str(self.A[i]) for i in range(self.n)) + "]"


class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new_node = SNode(x)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, x):
        new_node = SNode(x)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete_by_value(self, x):
        curr = self.head
        prev = None
        while curr:
            if curr.data == x:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return
            prev = curr
            curr = curr.next

    def traverse(self):
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elements) if elements else "Empty List")


class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, x):
        new_node = DNode(x)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def insert_after(self, target, x):
        curr = self.head
        while curr:
            if curr.data == target:
                new_node = DNode(x)
                new_node.next = curr.next
                new_node.prev = curr
                if curr.next:
                    curr.next.prev = new_node
                curr.next = new_node
                return
            curr = curr.next

    def delete_at_position(self, pos):
        if not self.head:
            return
        curr = self.head
        if pos == 0:
            self.head = curr.next
            if self.head:
                self.head.prev = None
            return
        for _ in range(pos):
            if not curr:
                return
            curr = curr.next
        if not curr:
            return
        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev

    def traverse(self):
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" <-> ".join(elements) if elements else "Empty List")


class Stack:
    def __init__(self):
        self.ll = SinglyLinkedList()

    def push(self, x):
        self.ll.insert_at_beginning(x)

    def pop(self):
        if not self.ll.head:
            return None
        value = self.ll.head.data
        self.ll.head = self.ll.head.next
        return value

    def peek(self):
        if not self.ll.head:
            return None
        return self.ll.head.data


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = SNode(x)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None
        value = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return value

    def front(self):
        if not self.head:
            return None
        return self.head.data


def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}
    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.peek() == pairs[ch]:
                stack.pop()
            else:
                return False
    return stack.peek() is None


if __name__ == "__main__":
    print("TASK 1: DYNAMIC ARRAY TEST")
    arr = DynamicArray(3)
    print("\nAppending 10 items:")
    for i in range(5, 15):
        arr.append(i)
    print("Final Array:", arr)
    print("Performing 2 pops:")
    arr.pop()
    arr.pop()
    print("Updated Array:", arr)

    print("\nTASK 2A: SINGLY LINKED LIST TEST")
    sll = SinglyLinkedList()
    sll.insert_at_beginning(5)
    sll.insert_at_beginning(15)
    sll.insert_at_beginning(25)
    sll.insert_at_end(50)
    sll.insert_at_end(60)
    sll.insert_at_end(70)
    print("\nAfter insertions:")
    sll.traverse()
    sll.delete_by_value(50)
    print("After deleting 50:")
    sll.traverse()

    print("\nTASK 2B: DOUBLY LINKED LIST TEST")
    dll = DoublyLinkedList()
    dll.insert_at_end("P")
    dll.insert_at_end("Q")
    dll.insert_at_end("R")
    print("\nInitial DLL:")
    dll.traverse()
    dll.insert_after("Q", "Z")
    print("After inserting Z after Q:")
    dll.traverse()
    dll.delete_at_position(2)
    print("After deleting position 2:")
    dll.traverse()

    print("\nTASK 4: PARENTHESES CHECKER TEST")
    test_cases = ["{[]}", "{[(])}", "(()", ""]
    for expr in test_cases:
        result = "Balanced" if is_balanced(expr) else "Not Balanced"
        print(f"Input: '{expr}' -> Result: {result}")