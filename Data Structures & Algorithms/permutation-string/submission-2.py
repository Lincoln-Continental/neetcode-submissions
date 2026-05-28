class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = {}
        for letter in s1:
            counter1[letter] = 1 + counter1.get(letter, 0)

        needed = len(counter1)
        for i in range(len(s2)):
            counter2 = {}
            current_match = 0

            for j in range(i, len(s2)):
                counter2[s2[j]] = 1 + counter2.get(s2[j], 0)

                if counter1.get(s2[j], 0) < counter2[s2[j]]:
                    break
                if counter1.get(s2[j], 0) == counter2[s2[j]]:
                    current_match += 1
                if current_match == needed:
                    return True
        return False