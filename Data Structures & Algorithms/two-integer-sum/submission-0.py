class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexHash = {}

        for i in range(len(nums)):
            indexHash[nums[i]] = i


        for i,n in enumerate(nums):
            diff = target - n

            if diff in indexHash and indexHash[diff] != i:
                return [i, indexHash[diff]]