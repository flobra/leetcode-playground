# /leetcode_problems/problem_1671.py
# Solution for Leetcode Problem #300: Minimum Number of Removals to Make Mountain Array
#
# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array

class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        
        n = len(nums)
        LIS = [1] * n
        LDS = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    LDS[i] = max(LDS[i], LDS[j] + 1)

        return n - max([LIS[i] + LDS[i] - 1 if LIS[i] > 1 and LDS[i] > 1 else 0 for i in range(n)])