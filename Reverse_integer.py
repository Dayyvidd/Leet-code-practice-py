class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
        for item in y:
            if x >= 0:
                rev_string = int(y[::-1])
            else:
                rev_string = -(int(y[-1:0:-1]))
            if rev_string > (2**31) or rev_string < -(2**31):
                return 0
            else:
                break
        return int(rev_string)

"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range
[-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers
(signed or unsigned).

"""
