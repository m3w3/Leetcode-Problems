"""
763. Partition Labels
https://leetcode.com/problems/partition-labels/
"""

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        part_labels = []
        char_last_i = characters_last_index(S)
        part_start, part_end = 0, char_last_i[S[0]]
        
        for i, char in enumerate(S):
            if i == part_end: # current partition has met its end
                part_labels.append(i + 1 - part_start)
                
                part_start = i + 1
                if part_start < len(S):
                    part_end = char_last_i[S[part_start]]
                continue
            if part_end < char_last_i[char]: 
                part_end = char_last_i[char] # extend where the partition ends
        
        return part_labels

def characters_last_index(S: str) -> dict:
    char_last_i = {}
    for i, char in enumerate(S):
        if char not in char_last_i: char_last_i[char] = i
        else: char_last_i[char] = i
    return char_last_i
