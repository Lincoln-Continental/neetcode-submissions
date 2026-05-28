class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}

        for i, n in enumerate(nums):
            nums_map[n] = 1 + nums_map.get(n, 0)

        arr = []
        for num, cnt in nums_map.items():
            arr.append([cnt, num])
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        return result
        