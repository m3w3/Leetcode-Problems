class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # init DP array
        arr = [[None for col in range(len(grid[0]))] for row in range(len(grid))]
        # base cases
        arr[0][0] = grid[0][0]
        for r in range(1, len(grid)):
            arr[r][0] = arr[r - 1][0] + grid[r][0]
        for c in range(1, len(grid[0])):
            arr[0][c] = arr[0][c - 1] + grid[0][c]
        
        # recursive step
        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                arr[r][c] = min(arr[r-1][c], arr[r][c-1]) + grid[r][c]
        
        return arr[-1][-1]