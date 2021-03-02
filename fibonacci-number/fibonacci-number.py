class Solution:
    def fib(self, n: int) -> int:
        if n < 2: return n
        arr = [None for num in range(n+1)]
        arr[0], arr[1] = 0, 1
        for i in range(2, n+1):
            arr[i] = arr[i - 1] + arr[i - 2]
        return arr[-1]