# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         nums = nums
#         target = target
#
#         for num1, num2 in enumerate(nums):
#             if target - num2 in nums[num1 + 1:]:
#                 return num1, nums[num1 + 1:].index(target - num2) + num1 + 1

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """



solution = Solution()
a = "({}{)(}"
solution.longestCommonPrefix(a)