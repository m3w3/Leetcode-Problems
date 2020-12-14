class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        char_last_i, part_labels = {}, []
        for i, char in enumerate(S):
            if char not in char_last_i: char_last_i[char] = i
            else: char_last_i[char] = i
        
        part_start, part_end = 0, char_last_i[S[0]]
        for i, char in enumerate(S):
            if i == part_end:
                part_labels.append(i + 1 - part_start)
                part_start = i + 1
                if part_start < len(S):
                    part_end = char_last_i[S[part_start]]
                continue
            if part_end < char_last_i[char]: part_end = char_last_i[char]
        
        return part_labels
