"""
Determine whether an integer is a palindrome. An integer is a 
palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting 
the integer to a string?

 

Example 1:

Input: x = 121
Output: true

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, 
it becomes 121-. Therefore it is not a palindrome.
"""


class Solution(object):
    def isPalindrome(self, x):
        
        # reverse the string
        reverse = str(x)[::-1]
        print(reverse)

        if str(x) == reverse:
            # overflow check - this was a pain in python w/o libs
            if abs(int(reverse)) < 2**31 and int(reverse) != 2**31 - 1:
                return True
            else:
                return False
        else:
            return False


s1 = Solution

test_cases = [123, 1234, -123, 222222231, 23432]


for k in test_cases:
    print("{0}: {1}".format(k, s1.reverse(s1, k)))