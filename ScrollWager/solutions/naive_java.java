import java.io.*;
import java.util.*;

// public class Solution {
public class naive_java {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */

        Scanner input = new Scanner(System.in);
        int xDim = input.nextInt();

        //the simple change needed to make this naive solution work is
        // adding % 125 to the end of the below line ;)

        int yDim = input.nextInt();
        int[][] board = new int[yDim][xDim];
        for(int i = 0; i < xDim; i++)
        {
            board[0][i] = i%10;
        }
        for(int i = 1; i < yDim; i++)
        {
            for(int j = 1; j < xDim; j++)
            {
                board[i][j] = (board[i-1][j] + board[i-1][j-1] + board[i][j-1]) %10;
            }
        }
        for (int w = 0; w < xDim; w++)
        {
            System.out.print(board[yDim-1][w] + " ");
        }
    }
}