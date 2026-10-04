class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexhash = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in indexhash:
                return [indexhash[diff], i]

            indexhash[n] = i