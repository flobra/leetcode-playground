# algorithms/sorting/test_sorting.py
from algorithms.sorting.bubble_sort import bubble_sort

def test_bubble_sort():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
