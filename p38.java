import java.util.*;

public class p38{
    public static void main(String[] args){
        int max = 0;
        for (int i = 1; i < 10000; i++){
            int pan = pan(i);
            if (max < pan){max = pan;}
        }

        System.out.println(max);
    }

    private static int pan(int num){
        StringBuilder build = new StringBuilder();
        int count = 1;
        while(build.length() < 9){
            build.append(num * count);
            count++;
        }

        if (build.length() == 9 && unique(build.toString())){return Integer.valueOf(build.toString());}
        
        return 0;
    }

    //unique and has no zeros
    private static boolean unique(String s){
        int n = s.length();
        Set<Character> letters = new HashSet<Character>();

        for (int i = 0; i < n; i++){
            char c = s.charAt(i);
            if (c == '0'){return false;}
            letters.add(c);
        }
        
        return letters.size() == n;
    }


}