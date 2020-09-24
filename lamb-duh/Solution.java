import java.util.Scanner;

public class Solution
{

    public static void main(String args[])
    {
        Scanner input = new Scanner(System.in);
        int numCases = input.nextInt();
        for (int t = 0; t < numCases; ++t)
        {
            int answer = 0;
            int n = input.nextInt();
            int k = input.nextInt();
            for (int i = 0; i < n; i++)
            {
                answer += input.nextInt();
            }
            for (int i = 0; i < k; i++)
            {
                answer += input.nextInt() * n;
            }
            System.out.println(answer);
        }
        input.close();

    }

}
