# Problem: Print Repeated Number Triangle Pattern
# Difficulty: Easy

# Problem Statement:
# Given an integer n, print a number triangle pattern
# containing n rows.
#
# In each row:
# - Print the current row number repeatedly.
# - The number of times the number is printed
#   should be equal to the row number.
#
# The first row contains:
# 1
#
# The second row contains:
# 22
#
# The third row contains:
# 333
#
# and so on until the nth row.

# Examples:
# Input: n = 4
# Output:
# 1
# 22
# 333
# 4444

# Explanation:
# Each row prints the row number
# repeated row-number times.

# Input: n = 2
# Output:
# 1
# 22

# Explanation:
# The first row prints 1 once
# and the second row prints 2 twice.

# Approach:
# - Use an outer loop for rows from 1 to n.
# - For every row i, print the number i
#   repeated i times.
# - Use string multiplication for easy repetition.

# Time Complexity: O(n²)
# Space Complexity: O(1)

# Key Learning:
# - Pattern printing
# - Nested loop thinking
# - Repetition using string multiplication
# - Understanding row-based patterns

class Solution:
    def pattern4(self, n):
        for i in range(1, n + 1):
            print(str(i) * i)