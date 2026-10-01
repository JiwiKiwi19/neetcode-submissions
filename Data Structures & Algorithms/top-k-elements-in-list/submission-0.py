class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        arr = [[] for i in range (len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            arr[c].append(n)

        out = []
        for i in range(len(arr) - 1, 0, -1):
            for n in arr[i]:
                out.append(n)
                if len(out) == k:
                    return out