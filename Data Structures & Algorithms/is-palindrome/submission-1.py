class Solution:
    def isPalindrome(self, s: str) -> bool:
        another_str = []

        for symbol in s:
            if symbol.isalnum():
                another_str.append(symbol.lower())

        return another_str == another_str[::-1]