class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = 1
        left, right = 1, max(piles)

        while left <= right:
            k = (left + right) // 2

            totalTime = 0 
            for pile in piles:
                totalTime += math.ceil(float(pile) / k)

            if totalTime <= h:
                result = k
                right = k - 1
            else:
                left = k + 1
        return result
        