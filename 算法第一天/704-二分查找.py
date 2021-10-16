# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if target in nums :
#             return nums.index(target)
#         else:
#             return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right :
            mid = (left + right) // 2
            if nums[mid] > target :
                right = mid - 1
            elif nums[mid] < target :
                left = mid + 1
            else :
                return mid  
        return -1
