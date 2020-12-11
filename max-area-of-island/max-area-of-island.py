"""
695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        max_size = 0
        seen = set()
        for y in range(height):
            for x in range(width):
                if (x, y) not in seen and grid[y][x] == 1:
                    x_y_seen, x_y_size = dfs(grid, x, y, height, width)
                    max_size = max(max_size, x_y_size)
                    seen = seen.union(x_y_seen)
        return max_size
    
def dfs(grid, start_x, start_y, height, width):
    stack = [(start_x, start_y)]
    seen, size = {(start_x, start_y)}, 0
    while stack:
        curr_x_y = stack.pop()
        size += 1
        curr_neighbours = neighbours(grid, curr_x_y, height, width)
        for (x, y) in curr_neighbours:
            if (x, y) not in seen and grid[y][x] == 1:
                stack.append((x, y))
                seen.add((x, y))
    return seen, size

def neighbours(grid, curr_x_y, height, width):
    l_ = []
    x, y = curr_x_y
    if x - 1 >= 0:      l_.append((x - 1, y))
    if x + 1 < width:   l_.append((x + 1, y))
    if 0 <= y - 1:      l_.append((x, y - 1))
    if y + 1 < height:  l_.append((x, y + 1))
    return l_
