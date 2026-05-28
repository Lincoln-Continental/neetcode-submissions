class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []



        for i in range(len(numbers) - 1):
            tmp = target - numbers[i]

            left = 0
            right = len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2

                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]

                if numbers[mid] > tmp:
                    right = mid - 1
                else:
                    left = mid + 1
                    