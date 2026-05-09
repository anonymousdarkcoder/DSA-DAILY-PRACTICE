# Problem: Print Right Triangle Star Pattern
# Difficulty: Easy

# Problem Statement:
# Given an integer n, print a right-angled triangle star pattern containing n rows.
#
# In each row:
# - The number of stars (*) should be equal
#   to the current row number.
#
# The first row contains 1 star,
# the second row contains 2 stars,
# and so on until the nth row.

# Examples:
# Input: n = 4
# Output:
# *
# **
# ***
# ****

# Explanation:
# The pattern contains 4 rows.
# Each row prints stars equal to its row number.

# Input: n = 2
# Output:
# *
# **

# Explanation:
# The first row contains 1 star
# and the second row contains 2 stars.

# Approach:
# - Use a loop from 1 to n.
# - For every row number i,
#   print "*" repeated i times.
# - This gradually increases the number
#   of stars in each row.

# Time Complexity: O(n²)
# Space Complexity: O(1)

# Key Learning:
# - Basics of pattern printing
# - Nested loop thinking
# - Incremental pattern formation
# - String multiplication in Python

class Solution:
    def pattern2(self, n):
        for i in range(1, n + 1):
            print("*" * i)