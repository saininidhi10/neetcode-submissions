class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # TC: O(E*(V + E)), SC = O(V + E)
        # n = len(edges)
        # adj = [[] for _ in range(n+1)]

        # def dfs(node, par):
        #     if visit[node]:
        #         return True
            
        #     visit[node] = True
        #     for nei in adj[node]:
        #         if nei == par:
        #             continue
        #         if dfs(nei, node):
        #             return True
        #     return False

        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        #     visit = [False]*(n+1)

        #     if dfs(u, -1):
        #         return [u, v]
        
        # return []

        # Topo sort (Kahn's algo)
        n = len(edges)
        adj = [[] for _ in range(n+1)]
        indegree = defaultdict(int)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        queue = deque()
        for node, degree in indegree.items():
            if degree == 1:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    queue.append(nei)
        
        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v]:
                return [u, v]
        return []

        