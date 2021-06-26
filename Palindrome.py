class Solution:
    def isPalindrome(self, x: int) -> bool:
        convert_to_string = str(x)
        for item in convert_to_string:
            if convert_to_string[::-1] == convert_to_string:
                return True
            else:
                return False

"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.

"""
