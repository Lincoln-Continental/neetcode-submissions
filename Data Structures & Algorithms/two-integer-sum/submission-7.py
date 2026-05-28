class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}

        for i, n in enumerate(nums):
            hashtable[n] = i  

        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in hashtable and hashtable[needed] != i:
                return [i, hashtable[needed]]

        return [] 