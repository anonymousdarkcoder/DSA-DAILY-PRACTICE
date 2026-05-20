# Problem: Print Inverted Number Triangle Pattern
# Difficulty: Easy

# Problem Statement:
# Given an integer n, print an inverted number
# triangle pattern containing n rows.
#
# In each row:
# - Print numbers starting from 1
#   up to the current row limit.
# - The first row contains numbers from 1 to n.
# - The second row contains numbers from 1 to n-1.
# - Continue decreasing until the last row
#   contains only 1.

# Examples:
# Input: n = 4
# Output:
# 1234
# 123
# 12
# 1

# Explanation:
# The pattern starts with numbers from 1 to 4
# and decreases one number in every row.

# Input: n = 2
# Output:
# 12
# 1

# Explanation:
# The first row prints numbers from 1 to 2
# and the second row prints only 1.

# Approach:
# - Use an outer loop from n down to 1.
# - For every row i, print numbers
#   from 1 to i.
# - Use end="" to print numbers
#   on the same line.
# - Print a new line after each row.

# Time Complexity: O(n²)
# Space Complexity: O(1)

# Key Learning:
# - Nested loops
# - Reverse pattern printing
# - Number patterns
# - Using end="" in print statements

class Solution:
    def pattern6(self, n):
        for i in range(n, 0, -1):
            for j in range(1, i + 1):
                print(j, end="")

            print()