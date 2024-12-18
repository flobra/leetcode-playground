from leetcode_problems.problem_74 import Solution

def test_searchMatrix():
    s = Solution()
    assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
    assert not s.searchMatrix([[]], 5)
    assert not s.searchMatrix([[3]], 5)
    assert s.searchMatrix([[5]], 5)
    assert not s.searchMatrix([[1,1]], 2)
    assert s.searchMatrix([[1,2]], 2)
    assert not s.searchMatrix([[1],[4],[10]], 5)
    assert s.searchMatrix([[1],[5],[10]], 5)
    assert not s.searchMatrix([[1],[1]], 2)
    assert s.searchMatrix([[1],[2]], 2)
    assert s.searchMatrix([[-50,-43,-29], [-27,-24,-19], [-15,-8,0]], -8)
    assert not s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 57)
    assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 1)
    assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60)

def test_searchMatrixImproved():
    s = Solution()
    assert s.searchMatrixImproved([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
    assert not s.searchMatrixImproved([[]], 5)
    assert not s.searchMatrixImproved([[3]], 5)
    assert s.searchMatrixImproved([[5]], 5)
    assert not s.searchMatrixImproved([[1,1]], 2)
    assert s.searchMatrixImproved([[1,2]], 2)
    assert not s.searchMatrixImproved([[1],[4],[10]], 5)
    assert s.searchMatrixImproved([[1],[5],[10]], 5)
    assert not s.searchMatrixImproved([[1],[1]], 2)
    assert s.searchMatrixImproved([[1],[2]], 2)
    assert s.searchMatrixImproved([[-50,-43,-29], [-27,-24,-19], [-15,-8,0]], -8)
    assert not s.searchMatrixImproved([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 57)
    assert s.searchMatrixImproved([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 1)
    assert s.searchMatrixImproved([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60)
