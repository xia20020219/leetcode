class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length

        def reverse(i, j):
            while i < j :
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        reverse(0, length - k - 1)
        reverse(length - k, length - 1)
        reverse(0, length - 1)
  
  # nums[: ] = (nums[i] for i in range(-(k % len(nums)), len(nums) - k % len(nums)))
  # https://leetcode-cn.com/problems/rotate-array/comments/  
    