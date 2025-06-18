class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i, v in enumerate(nums):
            expect = target - v
            if v in index:
                return [index[v], i]
            index[expect] = i

