class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in indices and indices[needed] != i:
                return [i, indices[needed]]
        return []