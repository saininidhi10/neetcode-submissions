class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        m, n = len(grid), len(grid[0])
        queue = deque()
        dirs = [(0,1), (1, 0), (-1, 0), (0, -1)]
        fresh = 0
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
        
        while fresh > 0 and queue:
            length = len(queue)

            for i in range(length):
                r, c = queue.popleft()
                
                for dr, dc in dirs:
                    print(dr, dc)
                    nr, nc = r+dr, c+dc
                    if (0 <= nr < m) and (0 <= nc < n) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            minutes += 1
        
        return minutes if fresh == 0 else -1