import java.util.*;

public class p40 {
    public static void main(String[] args){
        int i = 1;
        String istr = ((Integer) i).toString();
        int count = 1;
        int start = 1;
        char[] tenpow = new char[7];
        
        while(count <= 1000000){
            if (count - start >= istr.length()){
                i++;
                start = count;
                istr = ((Integer) i).toString();
            }

            char c = istr.charAt(count - start);

            switch(count){
                case 1: tenpow[0] = c; break;
                case 10: tenpow[1] = c; break;
                case 100: tenpow[2] = c; break;
                case 1000: tenpow[3] = c; break;
                case 10000: tenpow[4] = c; break;
                case 100000: tenpow[5] = c; break;
                case 1000000: tenpow[6] = c; break;
            }
            
            count++;
        }

        int prod = 1;
        for (char c: tenpow){
            prod *= Integer.valueOf(c - 48);
        }

        System.out.println(prod);

    }
}
