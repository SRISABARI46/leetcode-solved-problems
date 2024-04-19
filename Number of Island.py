# For question see the description
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        island=0

        def island_check(grid,r,c):
            if r>=0 and r<len(grid) and c>=0 and c<len(grid[0]) and grid[r][c]=="1":
                grid[r][c]="0"
                island_check(grid,r,c+1)
                island_check(grid,r,c-1)
                island_check(grid,r-1,c)
                island_check(grid,r+1,c)
  
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    island+=1
                    island_check(grid,r,c)
        return island
