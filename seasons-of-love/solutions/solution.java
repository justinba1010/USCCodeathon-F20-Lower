import java.util.Scanner;

public class solution
{

    public static void main(String args[])
    {
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        String unit = input.next();
        if(unit.equals("s"))
        {
            System.out.println(num);
        }
        else if(unit.equals("m"))
        {
            System.out.println(num * 60);
        }
        else if(unit.equals("h"))
        {
            System.out.println(num * 60 * 60);
        }
        else if(unit.equals("d"))
        {
            System.out.println(num * 60 * 60 * 24);
        }
        else if(unit.equals("w"))
        {
            System.out.println(num * 60 * 60 * 24 * 7);
        }
        else if(unit.equals("mo"))
        {
            System.out.println(num * 60 * 60 * 24 * 7 * 30);
        }
        else if(unit.equals("mo"))
        {
            System.out.println(num * 60 * 60 * 24 * 7 * 30 * 365);
        }
        
        input.close();

    }

}
