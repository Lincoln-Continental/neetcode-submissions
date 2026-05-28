class Solution:
    def longestConsecutive(self, nums):
        result = []
        
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if n - 1 not in num_set:
                cur = n
                length = 1

                while cur + 1 in num_set:
                    cur += 1
                    length += 1

                longest = max(longest, length)
        return longest
