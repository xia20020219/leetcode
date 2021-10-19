class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums : return 0
        count = collections.Counter(nums)
        keys = sorted(count)
        array = [0]
        for i, v in enumerate(keys) :
            if i > 0 and keys[i - 1] + 1 != v:
                array.append(0)
            array.append(count[v] * v)
        for i in range(2, len(array)):
            array[i] = max(array[i-2] + array[i], array[i - 1])
        return array[-1]
