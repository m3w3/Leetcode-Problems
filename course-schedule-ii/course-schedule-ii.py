"""
210. Course Schedule II
https://leetcode.com/problems/course-schedule-ii
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create the "visited status of 0, 1, 2. Start as 0s"
        # 0 -> never visited, 1 -> in the process of visiting, 2 -> visited
        visited = [0 for _ in range(numCourses)]
        # create adjacency list of pre-req -> course
        prereq_graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites: prereq_graph[prereq].append(course)
        
        course_order = []
        for prereq in range(numCourses):
            # prereq can only be 0, 2, never 1.
            if visited[prereq] == 2: continue
            # else, perform DFS on node prereq
            visited, course_order = dfs(prereq, prereq_graph, visited, course_order)
            # if cycle detected, visited will return False
            if not visited: return []
        return course_order[::-1]

def dfs(prereq, prereq_graph, visited, course_order):
    # visited status needs to be updated
    visited[prereq] += 1
    for course in prereq_graph[prereq]:
        # dfs all the courses taken after prereq
        # before dfs the course, check:
        # already visited, so ignore
        if visited[course] == 2: continue
        # cycle, error
        elif visited[course] == 1: return False, []
        # only case that's appropriate to call dfs on is visited val==0
        visited, course_order = dfs(course, prereq_graph, visited, course_order)
        # if cycle detected, visited will return False
        if not visited: return False, []
    # finished visited all child courses of prereq
    visited[prereq] += 1
    # add prereq to course_order
    course_order.append(prereq)
    return visited, course_order
