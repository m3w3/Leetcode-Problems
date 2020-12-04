"""
819. Most Common Word
https://leetcode.com/problems/most-common-word/
"""
NON_LETTERS = dict(zip(" !?',;.", [1, 2, 3, 4, 5, 6, 7]))
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        n = len(paragraph)
        if n == 1: return paragraph[0] # guaranteed an answer
        p1, p2 = 0, 0
        seen = {}
        
        while p2 < n:
            p1_char, p2_char = paragraph[p1], paragraph[p2]
            if is_alph(p1_char) and (p2 == n - 1 or not is_alph(p2_char)):
                if p2 == n - 1 and is_alph(p2_char): curr_word = paragraph[p1:].lower()
                else: curr_word = paragraph[p1:p2].lower()
                seen = add_word(seen, curr_word, banned)
                p2 += 1
                p1 = p2
            elif is_alph(p1_char) and is_alph(p2_char):
                p2 += 1
            elif not is_alph(p1_char) and not is_alph(p2_char):
                p1 += 1
                p2 += 1
            else:
                p1 += 1
​
        return most_count(seen)
​
def is_alph(char):
    return char not in NON_LETTERS
    
def add_word(seen, word, banned):
    if word not in banned:
        if word not in seen: seen[word] = 1
        else: seen[word] += 1
    
    return seen
​
def most_count(seen):
    max_count_word = [None, -1]
    for word in seen:
        word_count = seen[word]
        if word_count > max_count_word[1]:
            max_count_word = [word, word_count]
    return max_count_word[0]
