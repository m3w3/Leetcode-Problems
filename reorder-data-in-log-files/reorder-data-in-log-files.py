"""
937. Reorder Data in Log Files
https://leetcode.com/problems/reorder-data-in-log-files/
"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let_logs, dig_logs = [], []
        # split the logs into letters-only and digits-only
        for log in logs:
            if log.split()[1].isdigit(): dig_logs.append(log)
            else: let_logs.append(log)
        
        let_logs = merge_sort(let_logs)
        return let_logs + dig_logs

def merge_sort(let_logs):
    n = len(let_logs)
    # base case: when let_logs size is 1
    if n == 1: return let_logs
    # recursive case
    m = n // 2
    left, right = merge_sort(let_logs[:m]), merge_sort(let_logs[m:])
    return merge(left, right)

def merge(left, right):
    sorted_l = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if a_smaller_than_b(left[i], right[j]):
            sorted_l.append(left[i])
            i += 1
        else:
            sorted_l.append(right[j])
            j += 1
    
    # in case there are any residual lists of either left or right
    if i != len(left): return sorted_l + left[i:]
    elif j != len(right): return sorted_l + right[j:]
    else: return sorted_l

def a_smaller_than_b(a, b):
    a_list, b_list = a.split(), b.split()
    a_len, b_len = len(a_list), len(b_list)
    
    # skip index 0 since that's the identifier
    for i in range(1, min(a_len, b_len)):
        word_a, word_b = a_list[i], b_list[i]
        if word_a < word_b: return True # then a < b
        elif word_b < word_a: return False # then b < a
    
    # which ever is shorter is smaller
    return True if a_len < b_len else False 
