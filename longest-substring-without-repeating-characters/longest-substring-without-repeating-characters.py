"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        seen = {}
        max_length, p1 = 0, 0
        for p2, char in enumerate(s):
            if char in seen and p1 <= seen[char]:
                p1 = seen[char] + 1
            else:
                max_length = max(max_length, p2 - p1 + 1)

            seen[char] = p2

        return max_length
