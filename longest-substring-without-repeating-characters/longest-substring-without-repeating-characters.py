"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "abcdcefg"
        # "a" -> "ab" -> "abc" -> "abcd" -> so far it's 4
        # hash = {}
        # "abcdc" -> c already visited (know this from hashmap)
        # "dc" -> "dce" -> "dcef" -> "dcefg" -> so far longest is 5
        # return 5
        
        n = len(s)
        if n == 0: return 0
        seen = {}
        p1 = 0
        max_len, curr_len = 0, 0
        for p2, char in enumerate(s):
            if char not in seen:
                seen[char] = p2
                curr_len += 1
                continue
            else:
                max_len = max(max_len, curr_len)
                p1 = seen[char] + 1
                curr_len = p2 - seen[char]
                seen = update(s, seen, p1, p2)
        
        return max(max_len, curr_len)
​
def update(s, seen, p1, p2):
    d = {}
    for i in range(p1, p2 + 1):
        curr_char = s[i]
        if curr_char not in d: d[curr_char] = i
    return d
