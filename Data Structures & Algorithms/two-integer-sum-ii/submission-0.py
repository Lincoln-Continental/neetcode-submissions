class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_hashmap = {}
        result = []

        for i, n in enumerate(numbers):
            num_hashmap[n] = i

        for i, n in enumerate(numbers):
            difference = target - n

            if difference in num_hashmap and num_hashmap[difference] != i:
                return [i+1, num_hashmap[difference]+1]
