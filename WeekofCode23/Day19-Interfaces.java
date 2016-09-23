import java.io.*;
import java.util.*;

interface AdvancedArithmetic{
   int divisorSum(int n);
}
// Create a class that adheres to AdvancedArithmetic here
class Calculator implements AdvancedArithmetic {
    public int divisorSum(int n) {
        i = 0
        for (x=1;x<=n;x++) {
            if (n % x == 0) {
                i = i + x;
            }
        }
        return i
    }
}
// end exercise
class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();
        
        AdvancedArithmetic myCalculator = new Calculator(); 
        int sum = myCalculator.divisorSum(n);
        System.out.println("I implemented: " + myCalculator.getClass().getInterfaces()[0].getName() );
        System.out.println(sum);
    }
}