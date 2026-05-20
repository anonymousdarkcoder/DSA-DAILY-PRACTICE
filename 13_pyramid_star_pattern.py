# Problem: Print Pyramid Star Pattern
# Difficulty: Easy

# Problem Statement:
# Given an integer n, print a centered pyramid star pattern
# containing n rows.
#
# Each row i (1-indexed) contains:
# - (n - i) leading spaces
# - (2*i - 1) stars (*)
#
# The pattern forms a symmetric pyramid shape.

# Examples:
# Input: n = 4
# Output:
#    *
#   ***
#  *****
# *******

# Explanation:
# Row-wise construction:
# Row 1 → 3 spaces + 1 star
# Row 2 → 2 spaces + 3 stars
# Row 3 → 1 space  + 5 stars
# Row 4 → 0 spaces + 7 stars

# Input: n = 2
# Output:
#  *
# ***

# Explanation:
# Row 1 → 1 space + 1 star
# Row 2 → 0 spaces + 3 stars

# Approach:
# - Use an outer loop for rows 1 to n.
# - Print (n - i) spaces to center align.
# - Print (2*i - 1) stars for pyramid shape.
# - Combine both in each row.

# Time Complexity: O(n²)
# Space Complexity: O(1)

# Key Learning:
# - Pattern decomposition (spaces + stars)
# - Mathematical relationship in patterns
# - Nested loops and string multiplication
# - Center-aligned pattern logic

class Solution:
    def pattern7(self, n):
        for i in range(1, n + 1):
            # Print leading spaces
            print(" " * (n - i), end="")

            # Print stars
            print("*" * (2 * i - 1))