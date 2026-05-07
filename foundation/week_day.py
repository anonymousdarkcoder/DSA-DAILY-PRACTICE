# Problem: Which Week Day
# Platform: Basic I/O / Switch Case
# Difficulty: Easy

# Problem Statement:
# Complete the function whichWeekDay which takes an integer 'day'
# and prints the corresponding day of the week.
# Week starts from Monday.
# If the value is less than 1 or greater than 7, print "Invalid".

# Examples:
# Input: 3
# Output: Wednesday

# Input: 8
# Output: Invalid

# Input: 2
# Output: Tuesday

# Approach:
# - Use Python's match-case statement (similar to switch-case).
# - Match values from 1 to 7 with weekdays.
# - Use default case (_) for invalid inputs.

# Time Complexity: O(1)
# Space Complexity: O(1)

# Key Learning:
# - Using match-case as a switch-case alternative in Python.
# - Handling default cases using underscore (_).

class Solution:
    def whichWeekDay(self, day):
        match day:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")
            case _:
                print("Invalid")