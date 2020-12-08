class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0]) # since len(grid) > 0
        if width == 0: return 0
        else:
            count = 0
            visited = set()
        
        for y in range(height):
            for x in range(width):
                if grid[y][x] == "1" and (x, y) not in visited:
                    just_visited = dfs(grid, (x, y), height, width)
                    visited = visited.union(just_visited)
                    count += 1
        return count
​
def dfs(grid, coordinate, height, width) -> set:
    visited = set([coordinate])
    stack = [coordinate]
    while len(stack) != 0:
        curr_x_y = stack.pop()
        for neighbour in neighbours(curr_x_y, height, width):
            if grid[neighbour[1]][neighbour[0]] == "1" and neighbour not in visited: 
                stack.append(neighbour)
                visited.add(neighbour)
    return visited
                
            
def neighbours(curr_x_y: tuple, max_height: int, max_width: int) -> List[tuple]:
    x, y = curr_x_y[0], curr_x_y[1]
    adjacent = []
    if x - 1 >= 0: 
        adjacent.append((x - 1, y))
    if y + 1 < max_height: 
        adjacent.append((x, y + 1))
    if x + 1 < max_width:
        adjacent.append((x + 1, y))
    if y - 1 >= 0: 
        adjacent.append((x, y - 1))
    return adjacent
