class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0 # right - left + 1
        letter_frequency = {} # letter:count

        left = 0
        max_frequency = 0
        for right in range(len(s)):
            letter_frequency[s[right]] = 1 + letter_frequency.get(s[right], 0)
            max_frequency = max(max_frequency, letter_frequency[s[right]])

            while (right - left + 1) - max_frequency > k:
                letter_frequency[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)

        return result
