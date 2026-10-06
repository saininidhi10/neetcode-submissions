class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_islands = 0
        m, n = len(grid), len(grid[0])
        visited = set()

        def bfs(grid, r, c):
            nonlocal visited, m, n
            queue = deque([(r, c)])
            
            while queue:
                row, col = queue.popleft()
                new_coords = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
                for coord in new_coords:
                    nr, nc = coord
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1' and (nr, nc) not in visited:
                        queue.append(coord)
                        visited.add(coord)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1' and (row, col) not in visited:
                    num_of_islands += 1
                    bfs(grid, row, col)
        
        return num_of_islands