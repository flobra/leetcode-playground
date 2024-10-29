from leetcode_problems.problem_424 import Solution

# Instantiate the Solution class
solution = Solution()

def test_basic_case():
    # Basic test cases
    assert solution.characterReplacement("ABBB", 2) == 4
    assert solution.characterReplacement("AABABBA", 1) == 4
    assert solution.characterReplacement("ABAB", 2) == 4

def test_all_identical_characters():
    # Test where all characters are identical
    assert solution.characterReplacement("AAAA", 2) == 4  # k should have no effect
    assert solution.characterReplacement("BBBB", 0) == 4  # k should have no effect

def test_all_unique_characters():
    # Test where all characters are unique
    assert solution.characterReplacement("ABCD", 2) == 3
    assert solution.characterReplacement("ABCDEF", 1) == 2
    assert solution.characterReplacement("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0) == 1  # No replacements allowed

def test_longer_repeating_patterns():
    # Test with longer strings and repeating patterns
    assert solution.characterReplacement("AABBBCCCDD", 3) == 6  # Transform to "BBBBBBCC"
    assert solution.characterReplacement("AABBBCCCBB", 5) == 10  # Almost entire string can be transformed
    assert solution.characterReplacement("AABBBAABB", 2) == 7  # Can make almost all "B"

def test_no_replacements_needed():
    # Test where no replacements are needed because `k` is high enough
    assert solution.characterReplacement("AABBB", 3) == 5  # All can become "B" without limit
    assert solution.characterReplacement("ABABABAB", 4) == 8  # All can become either "A" or "B"

def test_edge_cases():
    # Edge cases with empty string and single characters
    assert solution.characterReplacement("", 2) == 0  # Empty string
    assert solution.characterReplacement("A", 2) == 1  # Single character, no replacements needed
    assert solution.characterReplacement("AB", 0) == 1  # No replacements allowed, only one character matches

def test_large_k():
    # Cases with `k` greater than the string length
    assert solution.characterReplacement("AABBB", 10) == 5  # `k` allows complete transformation
    assert solution.characterReplacement("ABCD", 10) == 4  # `k` allows complete transformation

def test_large_input():
    # Test with a larger input to ensure performance for valid window calculation
    long_string = "A" * 1000 + "B" * 1000
    assert solution.characterReplacement(long_string, 500) == 1500  # Can replace 500 to extend "A"