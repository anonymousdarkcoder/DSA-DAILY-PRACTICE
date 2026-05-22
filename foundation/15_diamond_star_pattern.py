# Problem: Print Diamond Star Pattern
# Difficulty: Easy

# Problem Statement:
# Given an integer n, print a diamond-shaped star pattern.
#
# The pattern consists of:
# - An upper pyramid of n rows
# - Followed by an inverted pyramid of n rows
#
# For each row:
# - Spaces are used for center alignment
# - Stars increase in the upper half
# - Stars decrease in the lower half

# Examples:
# Input: n = 4
# Output:
#    *
#   ***
#  *****
# *******
# *******
#  *****
#   ***
#    *

# Explanation:
# The first 4 rows form a normal pyramid.
# The next 4 rows form an inverted pyramid.

# Input: n = 2
# Output:
#  *
# ***
# ***
#  *

# Explanation:
# The upper half increases stars,
# and the lower half decreases stars.

# Approach:
# - First print the normal pyramid:
#   - Spaces decrease
#   - Stars increase by 2 each row
# - Then print the inverted pyramid:
#   - Spaces increase
#   - Stars decrease by 2 each row

# Time Complexity: O(n²)
# Space Complexity: O(1)

# Key Learning:
# - Combining multiple patterns
# - Pyramid and inverted pyramid logic
# - Symmetric pattern construction
# - Nested loop understanding

class Solution:
    def pattern9(self, n):

        # Upper pyramid
        for i in range(1, n + 1):
            print(" " * (n - i), end="")
            print("*" * (2 * i - 1))

        # Lower inverted pyramid
        for i in range(1, n + 1):
            print(" " * (i - 1), end="")
            print("*" * (2 * (n - i) + 1))