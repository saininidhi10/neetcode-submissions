class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        result = []
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c, visited, prev_height):
            if (r, c) in visited or r < 0 or r == ROWS or c < 0 or c == COLS or heights[r][c] < prev_height:
                return
            visited.add((r, c))
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                dfs(nr, nc, visited, heights[r][c])            

        for col in range(COLS):
            dfs(0, col, pac, heights[0][col])
            dfs(ROWS-1, col, atl, heights[ROWS-1][col])
        
        for row in range(ROWS):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, COLS-1, atl, heights[row][COLS-1])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])
        
        return result