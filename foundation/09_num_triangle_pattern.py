# Problem: Print Number Triangle Pattern
# Difficulty: Easy

# Problem Statement:
# Given an integer n, print a number triangle pattern
# containing n rows.
#
# In each row:
# - Print numbers starting from 1
#   up to the current row number.
#
# The first row contains:
# 1
#
# The second row contains:
# 12
#
# The third row contains:
# 123
#
# and so on until the nth row.

# Examples:
# Input: n = 4
# Output:
# 1
# 12
# 123
# 1234

# Explanation:
# Each row prints numbers from 1
# up to the current row number.

# Input: n = 2
# Output:
# 1
# 12

# Explanation:
# The first row prints 1
# and the second row prints 12.

# Approach:
# - Use an outer loop for rows from 1 to n.
# - Use an inner loop to print numbers
#   from 1 to the current row number.
# - Use end="" to print numbers on the same line.
# - Print a new line after each row.

# Time Complexity: O(n²)
# Space Complexity: O(1)

# Key Learning:
# - Nested loops
# - Pattern printing with numbers
# - Using end="" in print statements
# - Understanding row-column relationships

class Solution:
    def pattern3(self, n):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end="")

            print()