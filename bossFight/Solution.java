import java.util.*;
public class Solution {
    public static void main(String args[]) {
        //Solution purposely made with approaches that 145/146 students would know
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        // String[] symbols = {"+", "-", "*", "/"}
        String lettersSeen = "";
        for (int i = 0; i < cases; i++) {
            int a = sc.nextInt();
            String letter = sc.next();
            int b = sc.nextInt();
            String equalSign = sc.next();
            int c = sc.nextInt();
            // System.out.println(a+ letter+ b+equalSign+c);
            if (lettersSeen.contains(letter))
                System.out.println("seen");
            else
            {
                lettersSeen += letter;
                if (a + b == c)
                    System.out.print("+");
                if (a - b == c)
                    System.out.print("-");
                if (a * b == c)
                    System.out.print("*");
                if (b!= 0 && a % b == 0 && a / b == c)
                    System.out.print("/");
                System.out.println();
            }

        }
        

    }
}