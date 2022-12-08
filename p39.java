import java.util.*;

public class p39 {
    private static int[] mem = new int[1000];

    static{
        Arrays.fill(mem,-1);
    }

   public static void main(String[] args){
        int max = 0;
        int pval = 0;

        for (int i =1; i< 1000; i++){
            int temp = total(i);
            if (max < temp){max = temp; pval = i;}
        }

        System.out.println(pval);
   }

   private static int primitive(int p){
        if (mem[p] != -1){return mem[p];}
        int count = 0; 

        if(p %2 != 0){
            mem[p] = count;
            return count;
        }

        for (int i = 1; i <= Math.sqrt(p)/2; i++){
            double d = (Math.sqrt(i*i + 2*p) - i)/2;
            if (d > 0 && d % 1 == 0){
                int m = (int) d;
                if (m <= i) {continue;}
                if (m % 2 == i % 2){continue;}
                if (gcd(m,i) != 1){continue;}
                count++;
            }
        }

        mem[p] = count;
        return count;
   }

   private static int total(int p){
        int total = 0;
        for (int i = 1; i <= p/2; i++){
            if (p % i == 0) total += primitive(i);
        }

        return total;
   }

   //a > b
   private static int gcd(int a, int b){return b == 0 ? a : gcd(b, a%b);}
}
