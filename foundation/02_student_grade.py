# Problem: Student Grade
# Difficulty: Easy

# Problem Statement:
# Complete the function studentGrade which takes an integer 'marks' and prints the corresponding grade based on specific thresholds.

# Examples:
# Input: 95
# Output: Grade A

# Input: 70
# Output: Grade B

# Input: 14
# Output: Fail

# Approach:
# - Use if-elif-else ladder to check marks against thresholds in descending order.
# - Print the corresponding Grade string.

# Time Complexity: O(1)
# Space Complexity: O(1)

# Key Learning:
# - Conditional logic (if-elif-else) handling in Python.

class Solution:
    def studentGrade(self, marks):
        if marks >= 90:
            print("Grade A")
        elif marks >= 70:
            print("Grade B")
        elif marks >= 50:
            print("Grade C")
        elif marks >= 35:
            print("Grade D")
        else:
            print("Fail")