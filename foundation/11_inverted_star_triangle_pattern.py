# Problem: Print Inverted Star Triangle Pattern
# Difficulty: Easy

# Problem Statement:
# Given an integer n, print an inverted right-angled
# triangle star pattern containing n rows.
#
# In each row:
# - Print stars (*) in decreasing order.
# - The first row contains n stars.
# - The second row contains n-1 stars.
# - Continue decreasing until the last row
#   contains only 1 star.

# Examples:
# Input: n = 4
# Output:
# ****
# ***
# **
# *

# Explanation:
# The pattern starts with 4 stars
# and decreases by one star in every row.

# Input: n = 2
# Output:
# **
# *

# Explanation:
# The first row contains 2 stars
# and the second row contains 1 star.

# Approach:
# - Use a loop starting from n down to 1.
# - For every row i, print "*" repeated i times.
# - This creates a decreasing star pattern.

# Time Complexity: O(n²)
# Space Complexity: O(1)

# Key Learning:
# - Pattern printing using loops
# - Reverse iteration
# - Decreasing patterns
# - String multiplication in Python

class Solution:
    def pattern5(self, n):
        for i in range(n, 0, -1):
            print("*" * i)