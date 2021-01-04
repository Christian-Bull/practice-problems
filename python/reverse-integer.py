"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store 
integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function 
returns 0 when the reversed integer overflows.

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

"""


class Solution(object):
    def reverse(self, x):
        
        # check if it's negative
        if x < 0:
            i = str(x)[1:]
            reverse = i[::-1]
            reverse = int('-{0}'.format(reverse))
        # assume it's positive
        else:
            reverse = int(str(x)[::-1])
        
        # overflow check - this was a pain in python w/o libs
        if abs(reverse) < 2**31 and reverse != 2**31 - 1:
            return reverse
        else:
            return 0


s1 = Solution

testCases = [234, 123, -123, 120, 0, 1534236469, 1563847412]

for k in testCases:
    print("{0}: {1}".format(k, s1.reverse(s1, k)))
