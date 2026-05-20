# Problem: Print Inverted Pyramid Star Pattern
# Difficulty: Easy

# Problem Statement:
# Given an integer n, print an inverted centered pyramid pattern.
#
# Each row i (1-indexed) contains:
# - (i - 1) leading spaces
# - (2 * (n - i) + 1) stars (*)
#
# The pattern starts with the widest row and reduces
# the number of stars by 2 in each subsequent row.

# Examples:
# Input: n = 4
# Output:
# *******
#  *****
#   ***
#    *

# Explanation:
# Row-wise breakdown:
# Row 1 → 0 spaces + 7 stars
# Row 2 → 1 space  + 5 stars
# Row 3 → 2 spaces + 3 stars
# Row 4 → 3 spaces + 1 star

# Input: n = 2
# Output:
# ***
#  *

# Explanation:
# Row 1 → 0 spaces + 3 stars
# Row 2 → 1 space  + 1 star

# Approach:
# - Use a loop from 1 to n for rows.
# - Print increasing spaces (i - 1).
# - Print decreasing stars (2*(n - i) + 1).
# - Combine both for each row.

# Time Complexity: O(n²)
# Space Complexity: O(1)

# Key Learning:
# - Inverted pyramid decomposition
# - Relationship between row index and stars
# - Pattern symmetry reasoning
# - Space + star balancing logic

class Solution:
    def pattern8(self, n):
        for i in range(1, n + 1):
            print(" " * (i - 1), end="")
            print("*" * (2 * (n - i) + 1))