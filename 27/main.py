class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        ret = [i for i in nums if i != val]
        for i in range(len(ret)):
            nums[i] = ret[i]
        return len(ret)