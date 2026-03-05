class StackADT:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) == 0:
            return None
        return self.data.pop()

    def peek(self):
        if len(self.data) == 0:
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


def fib(n, stack):
    stack.push(f"fib({n})")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1, stack) + fib(n-2, stack)


def main():
    s = StackADT()

    s.push(10)
    s.push(20)
    s.push(30)

    print("Top:", s.peek())
    print("Size:", s.size())
    print("Pop:", s.pop())
    print("Size after pop:", s.size())

    print("\nFibonacci Recursion Trace")

    trace = StackADT()
    n = 5
    result = fib(n, trace)

    print("Fibonacci:", result)

    while not trace.is_empty():
        print(trace.pop())


if __name__ == "__main__":
    main()