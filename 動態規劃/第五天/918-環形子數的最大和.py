class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        preMax = preMin = maxAns = minAns = 0
        if max(nums)<=0:
            return max(nums)
        for i in nums:
            preMax = max(i,preMax+i)
            preMin = min(i,preMin+i)
            maxAns = max(maxAns,preMax)
            minAns = min(minAns,preMin)
        return max(maxAns,sum(nums)-minAns)

# 取自 https://leetcode-cn.com/problems/maximum-sum-circular-subarray/solution/python-shuang-90-on-by-lsh40-an2n/
