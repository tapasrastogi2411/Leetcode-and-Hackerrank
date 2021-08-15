package Medium_Difficulty.Number_of_Islands;

public class NumberOfIslands {

    public void callDFS(char[][] grid, int row, int col){

        if(row < 0 || col < 0 || row >= grid.length || col >= grid[0].length || grid[row][col] != '1'){
            return;
        }

        grid[row][col] = '0';

        callDFS(grid, row + 1, col);
        callDFS(grid, row - 1, col);
        callDFS(grid, row, col + 1);
        callDFS(grid, row, col - 1);
    }

    public int numIslands(char[][] grid){

        int numRows = grid.length;
        int numColumns = grid[0].length;

        int islandCount = 0;

        for(int i = 0; i < numRows; i++){
            for(int j = 0; j < numColumns; j++){

                if(grid[i][j] == '1'){

                    callDFS(grid, i, j);

                    islandCount += 1;

                }
            }
        }

        return islandCount;
    }

    public static void main(String[] args) {
        
        char[][] grid = {
            {'1','1','1','1','0'},
            {'1','1','0','1','0'},
            {'1','1','0','0','0'},
            {'0','0','0','0','0'}

        };

        NumberOfIslands islands = new NumberOfIslands();
        
        int result = islands.numIslands(grid);

        System.out.println(result);
    }

    
}