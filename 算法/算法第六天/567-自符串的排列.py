class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        counter1 = collections.Counter(s1)
        n = len(s2)
        left, right = 0, len(s1) - 1
        counter2 = collections.Counter(s2[0:right])

        while right < n :
            counter2[s2[right]] += 1
            if counter1 == counter2 : return True
            counter2[s2[left]] -= 1
            if counter2[s2[left]] == 0 :
                del counter2[s2[left]]
            left += 1
            right += 1
        return False

# 取自 https://leetcode-cn.com/problems/permutation-in-string/solution/zhu-shi-chao-xiang-xi-de-hua-dong-chuang-rc7d/
# 這題之後再回來看......