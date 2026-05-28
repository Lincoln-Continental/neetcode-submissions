class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = 0
        left, right = 1, max(piles)

        while left <= right:
            k = (left + right) // 2

            time = 0
            for pile in piles:
                time += math.ceil(float(pile) / k)

            if time <= h:
                result = k
                right = k - 1
            else:
                left = k + 1

        return result 