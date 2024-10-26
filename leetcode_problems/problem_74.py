# /leetcode_problems/problem_74.py
# Solution for Leetcode Problem #74: Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    # First solution
    # Time Complexity: O(n + m)
    # Space Complexity: O(1)
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        if not matrix or len(matrix[0]) == 0:
            return False

        if target > matrix[-1][-1]:
            return False

        row_pointer = 0
        column_pointer = 0

        while matrix[row_pointer][-1] < target:
            row_pointer += 1

        while matrix[row_pointer][column_pointer] <= target:
            if matrix[row_pointer][column_pointer] == target:
                return True
            column_pointer += 1

        return False

    # Improved solution
    #
    # Now, instead of first searching the row and then going through the columns,
    # just treat the 2D-Matrix as a sorted list, then do binary search.
    #
    # Time Complexity: O(log(n * m))
    # Space Complexity: O(1)
    def searchMatrixImproved(self, matrix: list[list[int]], target: int) -> bool:

        if not matrix or len(matrix[0]) == 0:
            return False

        rows, cols = len(matrix), len(matrix[0])

        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (low + high) // 2
            if matrix[mid // cols][mid % cols] < target:
                low = mid + 1
            elif matrix[mid // cols][mid % cols] > target:
                high = mid - 1
            else:
                return True

        return False
