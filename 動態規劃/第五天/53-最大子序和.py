class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        findthemax = [nums[0]]
        for i in range(1, len(nums)) :
            findthemax.append(max(findthemax[-1] + nums[i], nums[i]))
        return max(findthemax)