class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        for i in range(len(s)//2):
            empty = s[left]
            s[left] = s[right]
            s[right] = empty
            left += 1
            right -= 1