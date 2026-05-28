class Solution:
    def isValid(self, ch: chr) -> bool:
        return (ord('a') <= ord(ch) <= ord('z') or
            ord('A') <= ord(ch) <= ord('Z') or
            ord('0') <= ord(ch) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        new_str = ''.join([symbol.lower() for symbol in s if self.isValid(symbol)])
        return new_str == new_str[::-1]