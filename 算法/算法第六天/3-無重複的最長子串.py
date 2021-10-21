class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        right, ans = 0, 0
        for left in range(len(s)):
            while right < len(s) and s[right] not in occ :
                occ.add(s[right])
                right += 1
            if len(occ) > ans :
                ans = len(occ)
            occ.remove(s[left])
        return ans

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) <= 1 : return len(s)
#         set_s = {}
#         left, maxlen = 0, 0

#         for right in range(len(s)):
#             nowChar = s[right]
#             if nowChar in set_s :
#                 if set_s[nowChar] + 1 >= left :
#                     left = set_s[nowChar] + 1
#             set_s[nowChar] = right
#             maxlen = max(maxlen, right - left + 1)
#         return maxlen