class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s == "": return -1
        
        d = {}
        for i, char in enumerate(s):
            if char not in d:
                d[char] = [i]
            else:
                d[char].append(i)
        
        for char in d:
            if len(d[char]) == 1:
                return d[char][0]
        
        return -1
        
