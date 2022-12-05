import java.util.*;

public class p37 {
    public static void main(String[] args){
        int count = 11;
        int sum =0;
        int i = 11;
        while(count != 0){
            inner:{
            for (int truncs :truncate(i)){
                if(!isPrime(truncs)){break inner;}
            }
            count--;
            sum += i;
            }
            i++;
        }

        System.out.println(sum);
    }

    private static int[] truncate(final int n){
        StringBuilder s = new StringBuilder(((Integer) n).toString());
        int numdigits = s.length();
        int[] out = new int[2*numdigits -1];

        int m =n; 
        for (int i = 0; i < numdigits; i++){
            out[i] = m;
            m = m/10;
        }

        for (int i = numdigits; i < 2*numdigits -1; i++){
            s.delete(0,1);
            out[i] = Integer.valueOf(s.toString());
        }

        return out;
    }

    private static boolean isPrime(int n){
    if (n == 1){return false;}
    for (int i = 2; i <= Math.sqrt(n); i++){
        if (n % i == 0){return false;}
    }

    return true;}
}
