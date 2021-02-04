class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # so the num of unique paths at any point is:
        # -> unique_paths(m-1, n) + unique_paths(m, n-1)
        if m == 1 or n == 1: return 1
        arr = [[None for col in range(n)] for row in range(m)]

        # base case
        for i in range(m):
            arr[i][0] = 1
        for j in range(n):
            arr[0][j] = 1

        # bottom up
        for i in range(1, m):
            for j in range(1, n):
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

        return arr[m - 1][n - 1]