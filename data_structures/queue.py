# data_structures/queue.py

import threading

class Queue:

    def __init__(self):
        self.array = []

    def is_empty(self):
        return not self.array

    def __len__(self):
        return len(self.array)

    def peek(self):
        if self.array:
            return self.array[-1]
        else:
            raise Exception("peek() called on empty stack.")

    def enqueue(self, item):
        self.array.insert(0, item)

    def dequeue(self):
        if self.array:
            return self.array.pop()
        else:
            raise Exception("dequeue() called on empty stack.")

    def __str__(self):
        return str(self.array)

class OptimizedQueue:

    def __init__(self, maxsize=10):
        self.enqueue_stack = []
        self.dequeue_stack = []
        self.maxsize = maxsize
        self.lock = threading.Lock()

    def is_empty(self):
        return not self.enqueue_stack and not self.dequeue_stack

    def __len__(self):
        return len(self.enqueue_stack) + len(self.dequeue_stack)

    def peek(self):
        if self.dequeue_stack:
            return self.dequeue_stack[-1]  # The front is the last item of dequeue stack
        elif self.enqueue_stack:
            return self.enqueue_stack[0]  # If dequeue stack is empty, the first item in enqueue stack is the front
        else:
            raise Exception("front() called on empty queue.")

    def enqueue(self, item):
        if len(self) == self.maxsize:
            raise Exception("Queue is full!")
        with self.lock:
            self.enqueue_stack.append(item)

    def dequeue(self):
        with self.lock:
            if self.is_empty():
                raise Exception("dequeue() called on empty queue.")
            if not self.dequeue_stack:
                # Transfer elements from enqueue_stack to dequeue_stack
                while self.enqueue_stack:
                    self.dequeue_stack.append(self.enqueue_stack.pop())
            return self.dequeue_stack.pop()

    def __str__(self):
        return f"enqueue_stack: {self.enqueue_stack}, dequeue_stack: {self.dequeue_stack}"

class OptimizedQueueNoLock:

    def __init__(self, maxsize=10):
        self.enqueue_stack = []
        self.dequeue_stack = []
        self.maxsize = maxsize

    def is_empty(self):
        return not self.enqueue_stack and not self.dequeue_stack

    def __len__(self):
        return len(self.enqueue_stack) + len(self.dequeue_stack)

    def peek(self):
        if self.dequeue_stack:
            return self.dequeue_stack[-1]  # The front is the last item of dequeue stack
        elif self.enqueue_stack:
            return self.enqueue_stack[0]  # If dequeue stack is empty, the first item in enqueue stack is the front
        else:
            raise Exception("front() called on empty queue.")

    def enqueue(self, item):
        if len(self) == self.maxsize:
            raise Exception("Queue is full!")
        self.enqueue_stack.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("dequeue() called on empty queue.")
        if not self.dequeue_stack:
            # Transfer elements from enqueue_stack to dequeue_stack
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

    def __str__(self):
        return f"enqueue_stack: {self.enqueue_stack}, dequeue_stack: {self.dequeue_stack}"

class CircularBufferQueue:
    def __init__(self, maxsize=10):
        self.maxsize = maxsize
        self.array = [None] * maxsize
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def full(self):
        return self.size == self.maxsize

    def peek(self):
        if self.size == 0:
            raise Exception("front() called on empty queue.")
        return self.array[self.front]

    def enqueue(self, item):
        if self.full():
            raise Exception("enqueue() called on full queue.")
        self.array[self.rear] = item
        self.rear = (self.rear + 1) % self.maxsize
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("dequeue() called on empty queue.")
        value = self.array[self.front]
        self.array[self.front] = None  # Optional: clear the slot
        self.front = (self.front + 1) % self.maxsize
        self.size -= 1
        return value

    def __str__(self):
        if self.is_empty():
            return "[]"
        # Display the queue in order from front to rear
        return str([self.array[(self.front + i) % self.maxsize] for i in range(self.size)])

