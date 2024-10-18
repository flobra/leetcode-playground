import pytest
from data_structures.queue import Queue, OptimizedQueue, OptimizedQueueNoLock, CircularBufferQueue

# Helper function to test a queue
def _test_queue_implementation(queue_cls, maxsize=None):
    if maxsize:
        queue = queue_cls(maxsize)
    else:
        queue = queue_cls()

    # Test isEmpty queue behavior
    assert queue.is_empty()
    assert len(queue) == 0
    with pytest.raises(Exception):
        queue.peek()  # Peek on an empty queue
    with pytest.raises(Exception):
        queue.dequeue()  # Dequeue on an empty queue

    # Enqueue elements
    for i in range(5):
        queue.enqueue(i)
        assert len(queue) == i + 1
        assert queue.peek() == 0

    # Test that enqueue beyond maxsize raises exception for fixed-size queues
    if maxsize:
        with pytest.raises(Exception):
            for i in range(maxsize):
                queue.enqueue(i + 5)

    # Dequeue elements
    if maxsize:
        for i in range(maxsize):
            assert queue.dequeue() == i
            assert len(queue) == maxsize - i - 1
    else:
        for i in range(5):
            assert queue.dequeue() == i
            assert len(queue) == 4 - i

    # Test dequeue on empty queue raises exception
    with pytest.raises(Exception):
        queue.dequeue()

    # Test peek after emptying the queue
    with pytest.raises(Exception):
        queue.peek()

    # Enqueue more elements and check the order again
    queue.enqueue(10)
    queue.enqueue(20)
    assert queue.peek() == 10
    assert queue.dequeue() == 10
    assert queue.dequeue() == 20

# Parametrize to test all 4 queue implementations
@pytest.mark.parametrize("queue_cls, maxsize", [
    (Queue, None),
    (OptimizedQueue, 10),
    (OptimizedQueueNoLock, 10),
    (CircularBufferQueue, 10),
])

def test_queues(queue_cls, maxsize):
    _test_queue_implementation(queue_cls, maxsize)

