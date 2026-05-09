# Problem: Sum of Numbers Using For Loop
# Difficulty: Easy

# Problem Statement:
# Complete the function forLoop which takes two integers 'low' and 'high' and returns the sum of all integers
# from low to high inclusive.

# Examples:
# Input: low = 1, high = 5
# Output: 15

# Explanation:
# 1 + 2 + 3 + 4 + 5 = 15

# Input: low = 3, high = 7
# Output: 25

# Explanation:
# 3 + 4 + 5 + 6 + 7 = 25

# Approach:
# - Initialize a variable 'total' to store the sum.
# - Use a for loop from low to high inclusive.
# - Add each number to 'total'.
# - Return the final sum.

# Time Complexity: O(n)
# Space Complexity: O(1)

# Key Learning:
# - Using for loops for range traversal.
# - Accumulating values using a running sum.

class Solution:
    def forLoop(self, low: int, high: int) -> int:
        total = 0

        for i in range(low, high + 1):
            total += i

        return total