import java.util.Scanner;

public class Solution
{

    public static void main(String args[])
    {
        Scanner input = new Scanner(System.in);
        int numCases = input.nextInt();
        for (int t = 0; t < numCases; ++t)
        {
            int n = input.nextInt();
            int k = input.nextInt();
            int[] sheep = new int[n];
//          int[] operations = new int[k];
            for (int i = 0; i < n; i++)
            {
                sheep[i] = input.nextInt();
            }
            for (int i = 0; i < k; i++)
            {
                int curOperation = input.nextInt();
                for (int j = 0; j < sheep.length; j++)
                {
                    sheep[j] += curOperation;
                }
//              sheep[i] = input.nextInt();
            }
            int total = 0;

            for (int i = 0; i < sheep.length; i++)
            {
                total += sheep[i];
            }
            System.out.println(total);
        }
        input.close();

    }

}
