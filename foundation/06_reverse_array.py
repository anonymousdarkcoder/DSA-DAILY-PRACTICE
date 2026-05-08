# Problem: Reverse Array In-Place
# Difficulty: Easy

# Problem Statement:
# Complete the function reverse which takes an array arr
# and reverses the array in-place.
# The changes should directly modify the original array
# without creating a new array.

# Examples:
# Input: arr = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Input: arr = [1,2,1,1,5,1]
# Output: [1,5,1,1,2,1]

# Approach:
# - Use two pointers:
#   left starting from index 0
#   right starting from the last index.
# - Swap elements at left and right positions.
# - Move left forward and right backward.
# - Since lists are mutable in Python,
#   changes happen directly on the original array
#   (pass by reference behavior).

# Time Complexity: O(n)
# Space Complexity: O(1)

# Key Learning:
# - Pass by reference behavior in Python lists
# - In-place modification
# - Two pointer technique
# - Swapping elements efficiently

class Solution:
    def reverse(self, arr: list) -> None:
        left = 0
        right = len(arr) - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]

            left += 1
            right -= 1