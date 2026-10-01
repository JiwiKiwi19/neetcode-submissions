class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexHash = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in indexHash:
                return [indexHash[diff], i]
            
            indexHash[n] = i 
        
        return
