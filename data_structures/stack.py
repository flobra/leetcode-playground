# data_structures/stack.py
class Stack:

    def __init__(self):
        self.array = []

    def empty(self):
        return not self.array

    def __len__(self):
        return len(self.array)

    def top(self):
        if self.array:
            return self.array[-1]
        else:
            raise Exception("top() called on empty stack.")

    def push(self, a):
        self.array.append(a)

    def pop(self):
        if self.array:
            return self.array.pop()
        else:
            raise Exception("pop() called on empty stack.")

    def __str__(self):
        return str(self.array)


