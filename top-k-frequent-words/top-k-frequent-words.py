"""
692. Top K Frequent Words
https://leetcode.com/problems/top-k-frequent-words/
"""

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_words, frequencies = {}, set()
        word_freq = word_frequencies(words)
        for word in words:
            curr_freq = word_freq[word]
            if curr_freq not in freq_words: 
                freq_words[curr_freq] = {word}
                frequencies.add(curr_freq)
            else: 
                freq_words[curr_freq].add(word)

        return_l = []
        frequencies = sorted(list(frequencies), reverse=True)
        
        for freq in frequencies:
            curr_words_len = len(freq_words[freq])
            freq_words[freq] = sorted(list(freq_words[freq]))
            if curr_words_len >= k:
                return return_l + freq_words[freq][:k]
            else:
                return_l += freq_words[freq]
                k -= curr_words_len
        return return_l

def word_frequencies(words: List[str]) -> dict:
    d = {}
    for word in words:
        if word not in d: d[word] = 1
        else: d[word] += 1
    return d
