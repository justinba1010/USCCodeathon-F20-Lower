import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        int count = input.nextInt();
        double average = 0;
        int[] grades = new int[count];
        for(int i = 0; i < count; i++)
        {
            int cur = input.nextInt();
            average += cur;
            grades[i] = cur;
        }
        // System.out.println(Arrays.toString(grades));
        Arrays.sort(grades);
                // System.out.println(Arrays.toString(grades));

        
        average = average / count;
        if(average >= 90)
            System.out.print("A ");
        else if(average >= 80)
            System.out.print("B ");
        else if(average >= 70)
            System.out.print("C ");
        else if(average >= 60)
            System.out.print("D ");
        else
            System.out.print("F ");
        
        double median = 0;
        if(grades.length % 2 == 0)
            median = (grades[grades.length/2 -1] + grades[grades.length/2]) / 2;
        else
            median = grades[grades.length/2];
        
        
        if(median >= 90)
            System.out.println("A");
        else if(median >= 80)
            System.out.println("B");
        else if(median >= 70)
            System.out.println("C");
        else if(median >= 60)
            System.out.println("D");
        else
            System.out.println("F");
            
        
    }
}