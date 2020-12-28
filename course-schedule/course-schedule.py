"""
207. Course Schedule
https://leetcode.com/problems/course-schedule/
"""
​
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        numCourses -> vertices
        prerequisites -> directed edges
        if no cycle -> true, else -> false
        graphs could be disconnected
        """
        graph = [[] for _ in range(numCourses)] # adjacency matrix init.
        status = [0 for _ in range(numCourses)] # 0 -> unvisited, 1 -> partial, 2 -> complete
        for x, y in prerequisites: graph[x].append(y) # fill the adj. matrix
        
        for course in range(numCourses):
            if status[course] > 0: continue
            status = dfs(course, graph, status)
            if not status: return False # check if cycle exists in current DFS call
        return True
        
def dfs(course, graph, status):
    status[course] += 1
    for prereq in graph[course]:
        if status[prereq] == 2: continue # prereq has been completely visited
        elif status[prereq] == 1: return False # prereq is ancestor -> cycle exists
        status = dfs(prereq, graph, status)
        if not status: return False # check if cycle exists in current DFS call
    status[course] += 1
    return status
