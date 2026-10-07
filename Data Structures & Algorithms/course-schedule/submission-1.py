class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS
        # pre_map = {i:[] for i in range(numCourses)}
        # for crs, pre in prerequisites:
        #     pre_map[crs].append(pre)
        # visited = set()

        # def dfs(crs):
        #     if crs in visited:
        #         return False
        #     if pre_map[crs] == []:
        #         return True

        #     visited.add(crs)
        #     for pre in pre_map[crs]:
        #         if not dfs(pre): return False
            
        #     visited.remove(crs)
        #     pre_map[crs] = []
        #     return True
        
        # for crs in range(numCourses):
        #     if not dfs(crs): return False
        
        # return True

        # Topological sort
        inDegree = [0]*numCourses
        adj = {i:[] for i in range(numCourses)}
        for src, dest in prerequisites:
            adj[src].append(dest)
            inDegree[dest] += 1
        
        queue = deque()
        for crs, deg in enumerate(inDegree):
            if deg == 0:
                queue.append(crs)
        
        finish = 0
        while queue:
            node = queue.popleft()
            finish += 1
            for nei in adj[node]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)
        
        return finish == numCourses