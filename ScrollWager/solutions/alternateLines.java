import java.io.*;
import java.util.*;
//naive solution
public class Solution
{

    public static void main(String[] args)
    {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        int width = input.nextInt();
        int height = input.nextInt();
        int[] line1 = new int[width];
        int[] line2 = new int[width];
        for (int i = 0; i < width; i++)
        {
            line1[i] = i % 10;
        }

        int curLine = 0;
        int lineToUse = 1;
        while (curLine < height)
        {
            lineToUse = 1;
            for (int w = 1; w < width; w++)
            {
                line2[w] =  (line1[w] + line1[w - 1] + line2[w - 1]) %10;
            }
            curLine++;
            if(curLine == height)
                break;

            lineToUse = 2;
            for (int w = 1; w < width; w++)
            {
                line1[w] =  (line2[w] + line2[w - 1] + line1[w - 1]) %10;
            }
            curLine++;
        }
        for (int w = 0; w < width; w++)
        {
            if(lineToUse == 1)
                System.out.print(line1[w] + " ");
            else
                System.out.print(line2[w] + " ");

            // line2[w] =  line1[w] + line1[w - 1] + line2[w - 1];
        }

    }
}