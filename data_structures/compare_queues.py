import time
from queue import Queue, OptimizedQueue, OptimizedQueueNoLock, CircularBufferQueue

# Function to test the operations on a given queue
def benchmark_queue(queue, num_operations=10000):
    start_time = time.time()

    # Enqueue operations
    for i in range(num_operations):
        queue.enqueue(i)

    # Peek operations
    for i in range(num_operations):
        queue.peek()

    # Dequeue operations
    for i in range(num_operations):
        queue.dequeue()

    end_time = time.time()
    return end_time - start_time

# Test the performance of both queues
def main():
    num_operations = 100000

    # Test Queue (non-optimized)
    q1 = Queue()
    time_q1 = benchmark_queue(q1, num_operations)
    print(f"Time taken for Queue (non-optimized) for {num_operations} operations: {time_q1:.5f} seconds")

    # Test OptimizedQueue
    q2 = OptimizedQueue(maxsize=num_operations)
    time_q2 = benchmark_queue(q2, num_operations)
    print(f"Time taken for OptimizedQueue for {num_operations} operations: {time_q2:.5f} seconds")

    # Test OptimizedQueueNoLock
    q3 = OptimizedQueueNoLock(maxsize=num_operations)
    time_q3 = benchmark_queue(q3, num_operations)
    print(f"Time taken for OptimizedQueueNoLock for {num_operations} operations: {time_q3:.5f} seconds")

    # Test OptimizedQueueNoLock
    q4 = CircularBufferQueue(maxsize=num_operations)
    time_q4 = benchmark_queue(q4, num_operations)
    print(f"Time taken for OpttimizedBufferQueue for {num_operations} operations: {time_q4:.5f} seconds")


if __name__ == "__main__":
    main()

