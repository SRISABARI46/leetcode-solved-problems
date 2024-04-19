# For question see the description
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        p=0    #perimenter
        c=0    #connection
        for i in range(0,row):
            for j in range(0,col):
                if grid[i][j]==1:
                    p+=4
                    if i!=0 and grid[i-1][j]==1:
                        c+=1
                    if j!=0 and grid[i][j-1]==1:
                        c+=1
        return (p-c*2)
        
