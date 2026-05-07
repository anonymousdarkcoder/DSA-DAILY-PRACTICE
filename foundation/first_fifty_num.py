# Problem: Sum of First 50 Numbers Ending With Digit d
# Platform: Basic I/O / While Loop
# Difficulty: Easy

# Problem Statement:
# Complete the function whileLoop which takes an integer 'd'
# (0 to 9) and returns the sum of the first 50 positive integers
# that end with digit d.

# Examples:
# Input: d = 1
# Output: 12300

# Explanation:
# The first 50 positive integers ending with 1 are:
# 1, 11, 21, 31, ..., 491
# Their sum is 12300.

# Input: d = 5
# Output: 12450

# Input: d = 2
# Output: 12350

# Approach:
# - Start checking numbers from 1.
# - Use a while loop until 50 valid numbers are found.
# - If a number ends with digit d (number % 10 == d),
#   add it to the sum.
# - Continue until count reaches 50.
# - Return the final sum.

# Time Complexity: O(n)
# Space Complexity: O(1)

# Key Learning:
# - Using while loops with conditions.
# - Checking last digit using modulo operator (%).
# - Maintaining count and cumulative sum.

class Solution:
    def whileLoop(self, d: int) -> int:
        count = 0
        num = 1
        total = 0

        while count < 50:
            if num % 10 == d:
                total += num
                count += 1

            num += 1

        return total