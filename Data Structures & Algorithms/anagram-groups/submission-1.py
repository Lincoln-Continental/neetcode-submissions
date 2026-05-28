class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for str in strs:
            result[tuple(sorted(str))].append(''.join(str))
            
        return list(result.values())
