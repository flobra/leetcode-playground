from leetcode_problems.problem_300 import Solution

def test_lengthOfLIS():
    s = Solution()
    assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
    assert s.lengthOfLIS([0,1,0,8,5,4,9]) == 4
    assert s.lengthOfLIS([0,5,1,6,2,7,3,8,4,9]) == 6
    assert s.lengthOfLIS([1]) == 1

