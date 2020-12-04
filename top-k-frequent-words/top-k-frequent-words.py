class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {} # word -> frequency
        l_ = []
        for word in words:
            if word not in d: d[word] = 1
            else: d[word] += 1
        d_reversed, counts = reversed_counts(d)
        d_reversed = sort_word_list(d_reversed)
        counts.sort()
        for count in counts[::-1]: # visit count in descending order of counts
            if k == 0: break
            curr_word_list = d_reversed[count]
            length_of_list = len(curr_word_list)
            if length_of_list <= k:
                l_ += curr_word_list
                k -= length_of_list
            else:
                l_ += curr_word_list[:k]
                break
        return l_
​
def reversed_counts(d):
    """
    >>> d = {'d': 2, 'c': 2, 'b': 1, 'a': 1}
    >>> reversed_counts(d, words)
    {2: ['d', 'c'], 1: ['b', 'a']}, [2, 1]
    """
    d_reversed = {} # frequency -> list of word(s)
    counts = [] # list of frequency counts
    for word in d:
        word_count = d[word]
        if word_count not in d_reversed:
            d_reversed[word_count] = [word]
            counts.append(word_count)
        else: d_reversed[word_count].append(word)
    return d_reversed, counts
​
def sort_word_list(d_reversed):
    """
    >>> d_reversed = {2: ['d', 'c'], 1: ['b', 'a']}
    >>> sort_Word_list(d_reversed)
    {2: ['c', 'd'], 1: ['a', 'b']}
    """
    for count in d_reversed:
        d_reversed[count].sort()
    return d_reversed
