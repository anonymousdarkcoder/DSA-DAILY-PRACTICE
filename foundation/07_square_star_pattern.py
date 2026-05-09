# Problem: Print Square Star Pattern
# Difficulty: Easy

# Problem Statement:
# Complete the function pattern1 which takes an integer n and prints a square pattern of stars (*) of size n × n.

# Examples:
# Input: n = 4
# Output:
# ****
# ****
# ****
# ****

# Input: n = 2
# Output:
# **
# **

# Approach:
# - Use a loop to print n rows.
# - In each row, print n stars using "*" * n.

# Time Complexity: O(n²)
# Space Complexity: O(1)

# Key Learning:
# - Nested pattern thinking
# - Using loops for pattern printing
# - String multiplication in Python

class Solution:
    def pattern1(self, n):
        # Loop through the range of n to create each row
        for i in range(n):
            # Print n stars for the current row
            print("*" * n)