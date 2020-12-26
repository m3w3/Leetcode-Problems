"""
692. Top K Frequent Words
https://leetcode.com/problems/top-k-frequent-words/
"""
from heapq import *
class Helper:
    def __init__(self, word, word_freq):
        self.word, self.word_freq = word, word_freq
    def __lt__(self, Helper2): # used to compare if self < Helper2
        if self.word_freq == Helper2.word_freq: 
            return self.word > Helper2.word
        return self.word_freq < Helper2.word_freq
    def __eq__(self, Helper2):
        return self.word == Helper2.word and self.word_freq == Helper2.word_freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = Counter(words)
        min_heap = []
        for word, freq in frequency.items():
            heappush(min_heap, Helper(word, freq))
            if len(min_heap) > k: 
                heappop(min_heap)
        return [heappop(min_heap).word for _ in range(len(min_heap))][::-1]
