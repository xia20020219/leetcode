class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i]
        return min(dp[-1], dp[-2])
# 我觉得这个题的描述应该改改：每个阶梯都有一定数量坨屎，一次只能跨一个或者两个阶梯，走到一个阶梯就要吃光上面的屎，问怎么走才能吃最少的屎？开局你选前两个阶梯的其中一个作为开头点，并吃光该阶梯的屎。
# 取自 https://leetcode-cn.com/problems/min-cost-climbing-stairs/comments/