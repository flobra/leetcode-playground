# /leetcode_problems/problem_300.py
# Solution for Leetcode Problem #300: Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        n = len(nums)
        LIS = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)

        return max(LIS)