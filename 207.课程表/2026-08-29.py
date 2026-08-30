from typing import List
from collections import deque,defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list) # 数据类型：创建的字典的值都是空列表
        indegree = [0]*numCourses # 入度：每门课程被指向的数目，即记录每门课程有几个前置课程
        count = 0

        for requery in prerequisites:
            pre = requery[1]
            course = requery[0]

            graph[pre].append(course)
            indegree[course]+=1

        queue = deque()
        for num in range(numCourses):
            if indegree[num] == 0:
                queue.append(num)

        while queue:
            course = queue.popleft()
            count += 1
            for next_course in graph[course]:
                indegree[next_course]-=1
                if indegree[next_course]==0:
                    queue.append(next_course)

        return count==numCourses