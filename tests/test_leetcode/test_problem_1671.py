from leetcode_problems.problem_1671 import Solution
import pytest

# Initialize the Solution instance
solution = Solution()

@pytest.mark.parametrize("nums, expected", [
    # Basic mountain case
    ([2, 1, 1, 5, 6, 2, 3, 1], 3),  # Expected to remove elements to form [2, 5, 6, 2]
    
    # No removals needed for already perfect mountain
    ([1, 2, 3, 4, 3, 2, 1], 0),  # Already a valid mountain
    
    # Only increasing or only decreasing sequences
    ([1, 2, 3, 4, 5], 5),  # Needs 4 removals to form any mountain
    ([5, 4, 3, 2, 1], 5),  # Needs 4 removals to form any mountain
    
    # Small cases
    ([1, 3, 2], 0),  # Smallest mountain
    ([2, 1], 2),  # Not enough elements to form a mountain
    
    # All elements are the same
    ([5, 5, 5, 5, 5], 5),  # All elements same, no mountain possible
    
    # Duplicate elements with a potential mountain
    ([2, 2, 2, 3, 4, 4, 4, 3, 2, 2], 5),  # Needs removals to form a mountain
    
    # Complex cases with multiple peaks
    ([1, 2, 1, 2, 3, 4, 3, 2, 1, 2, 1], 4),  # Expected to remove elements for single mountain
    
    # Cases with multiple increasing and decreasing subarrays
    ([9, 8, 1, 7, 6, 5, 6, 7, 8, 9, 3, 2, 1], 4),  # Needs 6 removals to form a mountain
    
    # Edge case with a larger mountain
    ([1, 3, 5, 7, 6, 4, 3, 2, 8, 9, 3, 1], 3),  # Expected to remove 4 elements for valid mountain
    
    # Single element
    ([1], 1),  # No mountain possible with one element
    
    # Two elements
    ([1, 2], 2),  # No mountain possible with two elements
    
    # Long increasing sequence followed by one element
    ([1, 2, 3, 4, 5, 4], 0),  # Remove 0 to form [1, 2, 3, 4, 5, 4] as mountain
    
    # Random mountain-like structure
    ([2, 4, 7, 3, 4, 6, 2, 3, 5, 4, 2, 1], 4),  # Remove elements to form a mountain
    
])

def test_minimumMountainRemovals(nums: list[int], expected: int):
    assert solution.minimumMountainRemovals(nums) == expected

