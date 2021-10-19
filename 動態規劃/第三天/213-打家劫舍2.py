class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 : return 0
        if len(nums) == 1 : return nums[-1]
        # 1 有 n 沒有
        pre1, pre2 = nums[0], 0
        for i in range(1, len(nums) - 1):
            pre2, pre1 = pre1, max(pre1, pre2 + nums[i])
        compare1 = max(pre1, pre2)

        # 1 沒有 n 有
        cur1, cur2 = nums[1], 0
        for i in range(2, len(nums)):
            cur2, cur1 = cur1, max(cur1, cur2 + nums[i])
        compare2 = max(cur1, cur2)
        return max(compare1, compare2)

