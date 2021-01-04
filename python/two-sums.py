"""
Given an array of integers nums and an integer target
return indices of the two numbers such that they add up to target

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Constraints:

    2 <= nums.length <= 103
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

"""

class Solution(object):
    def twoSum(self, nums, target):
        result = 0
        for index, value in enumerate(nums):
            # simple optimization, if i is greater than target -> skip
            if value > abs(target):
                continue
            else:
                for k, v in enumerate(nums):
                    # check for output and assign
                    if index != k and value + v == target:
                        return [index, k]

s1 = Solution

test = s1.twoSum(s1, [2,7,11,15], 9)
test2 = s1.twoSum(s1, [3,2,4], 6)
test3 = s1.twoSum(s1, [3,3], 6)

print(test)
print(test2)
print(test3)