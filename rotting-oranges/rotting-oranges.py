"""
994. Rotting Oranges
https://leetcode.com/problems/rotting-oranges/
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # go through grid once, put all rotten in queue
        # count total existing fresh oranges
        row, col = len(grid), len(grid[0])
        queue, fresh_count, time = deque(), 0, 0
        for y in range(row):
            for x in range(col):
                if grid[y][x] == 2: queue.append((y, x))
                elif grid[y][x] == 1: fresh_count += 1

        # perform BFS on each of the rotten oranges in queue
        while queue:
            # keep on popping queue as long as it's not empty
            # if we've reached here, time must've elapsed
            time += 1
            # only pop the rotten oranges CURRENTLY in queue
            # this is crucial since we're adding rotten ones during next time period
            for _ in range(len(queue)):
                y, x = queue.popleft() # the x,y coordinate of a rotten on grid
                # only add fresh oranges adjacent to it back into queue
                for next_y, next_x in adjacent_fresh_oranges(grid, y, x, row, col):
                    queue.append((next_y, next_x))
                    grid[next_y][next_x] = 2
                    fresh_count -= 1
        return -1 if fresh_count != 0 else max(0, time - 1)

def adjacent_fresh_oranges(grid, y, x, rows, columns):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    oranges = []
    for dy, dx in dirs:
        if 0 <= y + dy < rows and 0 <= x + dx < columns:
            if grid[y + dy][x + dx] == 1: oranges.append((y+dy, x+dx))
    return oranges