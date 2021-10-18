# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         findzero = 0
#         for i in range(len(nums)):
#             if nums[i]:
#                 nums[i], nums[findzero] = nums[findzero], nums[i]        
#                 findzero += 1 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return nums.sort(key = bool, reverse = True)   