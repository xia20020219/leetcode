class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right, pos = 0, n - 1, n - 1
        reset = [0] * n
        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                reset[pos] = nums[left] * nums[left]
                left += 1
            else:
                reset[pos] = nums[right] * nums[right]
                right -= 1
            pos -= 1
        return reset
