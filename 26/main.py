from sortedcontainers import SortedSet
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        ret = SortedSet(nums)
        for i in range(len(ret)):
            nums[i] = ret[i]
        return len(ret)