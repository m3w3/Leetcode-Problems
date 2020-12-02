"""
273. Integer to English Words
https://leetcode.com/problems/integer-to-english-words/
"""
ONES = 'Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve '\
       'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen Twenty'.split()
TENS = 'Zero Ten Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
​
THOUSANDS = 'Zero Thousand Million Billion Trillion'.split()
​
class Solution:
    def numberToWords(self, num: int) -> str:
        num_list = [int(digit) for digit in str(num)]
        n = len(num_list)
        
        num_three_blocks = n // 3
        num_leading_non_3s = n % 3
​
        if num == 0: return 'Zero'
        elif n <= 3: return str_length_3s(num_list) # 1 <= num <= 999
              
        # check if there are leading non blocks of 3s, i.e. 12,999,999 -> the 12
        l_ = []
        if num_leading_non_3s != 0:
            leading_non_3s = num_list[:num_leading_non_3s]
            l_.append(str_length_3s(leading_non_3s))
            l_.append(THOUSANDS[num_three_blocks])         
​
        for i in range(num_three_blocks): # i.e. 999,999,999 -> {0, 1, 2}, 22,999,222 -> {0, 1}
            curr_start_index = num_leading_non_3s + i*3 # i.e. 22,|999|,222 -> 2 + 0*3 = 2
            curr_length_3s = str_length_3s(num_list[curr_start_index: curr_start_index + 3])
            if curr_length_3s == '':
                continue
            l_.append(curr_length_3s)
            l_.append(THOUSANDS[num_three_blocks-1-i]) # <- appends 'Zero' in the final iteration
        
        if l_[-1] == 'Zero': return ' '.join(l_[:-1])
        else: return ' '.join(l_)
        
        
​
def str_length_3s(num_list: List[int]):
    """
    >>> str_leading([6])
    'Six'
    >>> str_leading([1, 2])
    'Twelve'
    >>> str_leading([1, 0, 0])
    'One Hundred'
    >>> str_leading([9, 5, 2])
    'Nine Hundred Fifty Two'
    >>> str_leading([0, 0, 0])
    ''
    >>> str_leading([0, 1, 2])
    'Twelve'
    """
    n = len(num_list) # could be 0, 1, 2, 3
    
    # since there're only 3 digits max, hard code it
    if n == 1:
        if num_list == [0]: return ''
        return ONES[num_list[0]]
    
    elif n == 2:
