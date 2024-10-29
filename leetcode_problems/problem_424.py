# /leetcode_problems/problem_424.py
# Leetcode Problem #424: Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)
        left = 0
        maxf = 0
        ans = 0
        count = {}

        for right in range(n):

            count[s[right]] = count.get(s[right], 0) + 1
            maxf = max(maxf, count[s[right]])

            if (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
            