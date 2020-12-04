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
            
            if curr_length_3s == '': continue # skip the '' or else they'll show up as extra spaces when joined
            l_.append(curr_length_3s)
            
            curr_suffix = THOUSANDS[num_three_blocks-1-i]
            if curr_suffix != 'Zero': l_.append(curr_suffix) # <- avoid appending 'Zero' in the final iteration
        
        return ' '.join(l_)
        
        
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
        if num_list[0] == 0: # i.e. [0, 1] -> 'One'
            return str_length_3s(num_list[1:])
        elif num_list[0] == 1: # i.e. [1, 7] -> 'Seventeen'
            return ONES[two_digit_to_num(num_list)]
        else: # i.e. [6, 1] -> 'Sixty One'
            ones_i = num_list[1]
            if ones_i == 0:
                return TENS[num_list[0]] # i.e. [6, 0] -> 'Sixty', not 'Sixty Zero'
            return ' '.join([TENS[num_list[0]], ONES[ones_i]])
​
    else:
        if num_list[0] == 0: # i.e. [0, 1, 6] -> 'Sixteen'
            return str_length_3s(num_list[1:])
        elif num_list[1] == 0 and num_list[2] == 0: # [6, 0, 0] -> 'Six Hundred'
            return ' '.join([ONES[num_list[0]], 'Hundred'])
        else: # i.e. [1, 1, 2] -> 'One Hundred Twelve'
            return ' '.join([ONES[num_list[0]], 'Hundred', str_length_3s(num_list[1:])])
​
        
def two_digit_to_num(two_digit_list: List[int]):
    """
    >>> two_digit_to_num([1, 2])
    12
    >>> two_digit_to_num([1, 8])
    18
    """
    l_ = [str(two_digit_list[0]), str(two_digit_list[1])]
    return int(''.join(l_))
