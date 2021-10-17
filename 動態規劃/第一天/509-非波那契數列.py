# class Solution:
#     def fib(self, n: int) -> int:
#         dp = [0, 1]
#         if n == 1 : return 1
#         else:
#             for i in range(2, n+1):
#                 dp.append(dp[i-1]+dp[i-2])
#             return dp[n]

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b

# https://leetcode-cn.com/problems/fibonacci-number/solution/qiu-fei-bo-na-qi-suan-fa-zheng-li-8ge-by-sq8k/
# 好像寫出來的網路上都有......