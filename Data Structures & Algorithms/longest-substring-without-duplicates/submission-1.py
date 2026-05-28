class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_set = set()
        length = 0

        left = 0
        for right in range(len(s)):
            while s[right] in str_set:
                str_set.remove(s[left])
                left += 1
            str_set.add(s[right])
            length = max(length, (right - left + 1))
        return length