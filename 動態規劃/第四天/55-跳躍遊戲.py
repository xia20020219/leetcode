class Solution:
    def canJump(self, nums: List[int]) -> bool:
        num, i = 0, 0
        if len(nums) == 1 : return True
        while i <= num :
            num = max(nums[i] + i, num)
            if num >= len(nums) - 1 : return True
            i += 1
        return False