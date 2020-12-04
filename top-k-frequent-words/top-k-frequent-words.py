"""
692. Top K Frequent Words
https://leetcode.com/problems/top-k-frequent-words/
"""

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d, l_ = {}, [] # word -> frequency, return list
        for word in words:
            if word not in d: d[word] = 1
            else: d[word] += 1
        # O(n)
        d_reversed, counts_desc = reversed_counts(d) # <- helper below
        # O(n) + O(n log n)
        for count in counts_desc: # visit count in descending order of counts
            curr_word_list = d_reversed[count]
            length_of_list = len(curr_word_list)
            if length_of_list <= k:
                l_ += curr_word_list
                k -= length_of_list
            else:
                l_ += curr_word_list[:k]
                break
        # O(n log n)
        return l_

def reversed_counts(d):
    """
    >>> d = {'d': 2, 'c': 2, 'b': 1, 'a': 1}
    >>> reversed_counts(d, words)
    {2: ['c', 'd'], 1: ['a', 'b']}, [2, 1]
    """
    d_reversed = {} # frequency -> list of word(s)
    counts = [] # list of frequency counts
    for word in d:
        word_count = d[word]
        if word_count not in d_reversed:
            d_reversed[word_count] = [word]
            counts.append(word_count)
        else: d_reversed[word_count].append(word)
    # O(n)
    
    # extra stuff below: also sort them here
    for count in d_reversed:
        d_reversed[count].sort()
    # O(n)
    counts.sort()
    # O(n log n)
    return d_reversed, counts[::-1]
