# Problem: Print Half Diamond Star Pattern
# Difficulty: Easy

# Problem Statement:
# Given an integer n, print a half-diamond star pattern.
#
# The pattern consists of:
# - An increasing right-angled triangle
# - Followed by a decreasing right-angled triangle
#
# The first part contains:
# - 1 star in the first row
# - increasing by 1 star per row until n stars
#
# The second part contains:
# - n-1 stars in the first row
# - decreasing by 1 star per row until 1 star

# Examples:
# Input: n = 4
# Output:
# *
# **
# ***
# ****
# ***
# **
# *

# Explanation:
# The pattern first increases stars
# from 1 to 4 and then decreases
# from 3 back to 1.

# Input: n = 2
# Output:
# *
# **
# *

# Explanation:
# The pattern increases to 2 stars
# and then decreases back to 1 star.

# Approach:
# - First print the increasing triangle:
#   stars increase from 1 to n.
# - Then print the decreasing triangle:
#   stars decrease from n-1 to 1.
# - Use string multiplication for stars.

# Time Complexity: O(n²)
# Space Complexity: O(1)

# Key Learning:
# - Combining increasing and decreasing patterns
# - Loop control for symmetric patterns
# - String multiplication in Python
# - Pattern construction logic

class Solution:
    def pattern10(self, n):

        # Increasing triangle
        for i in range(1, n + 1):
            print("*" * i)

        # Decreasing triangle
        for i in range(n - 1, 0, -1):
            print("*" * i)