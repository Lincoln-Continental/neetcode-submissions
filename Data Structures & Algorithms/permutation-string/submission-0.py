class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = {}
        for letter in s1:
            counter1[letter] = 1 + counter1.get(letter, 0)

        window_size = len(counter1)
        for i in range(len(s2)):
            counter2 = {}
            cur = 0
            for j in range(i, len(s2)):
                counter2[s2[j]] = 1 + counter2.get(s2[j], 0)
                if counter2[s2[j]] > counter1.get(s2[j], 0):
                    break
                if counter2[s2[j]] == counter1.get(s2[j], 0):
                    cur += 1
                if cur == window_size:
                    return True
        return False

