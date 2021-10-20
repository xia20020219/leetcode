class Solution:
    def jump(self, nums: List[int]) -> int:
        num, end, nowposition, step = len(nums), 0, 0, 0
        for i in range(num - 1):
            nowposition = max(nowposition, nums[i] + i)
            if i == end :
                end = nowposition
                step += 1
        return step