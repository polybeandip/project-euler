import java.util.*;

public class p26 {
    public static void main(String[] args){
        int max = 0;
        int d =0;
        for (int i = 2; i < 1000; i++){
            int howLong = howLong(i);
            if (max < howLong){
                max = howLong;
                d = i;
            }
        }

        System.out.println(d);
    }

    //if Im being honest, I barely know how this cluster fuck works. division is hard :(
    private static int howLong(final int n){
        Map<Integer, Integer> where = new HashMap<Integer,Integer>();
        where.put(0,0);
        int div = 1; 
        int count = 0;
        for (count = 0; true; count++){
            if(div < n){div *= 10; continue;}
            if (div >= n ){
                div = div %n;
                if (where.containsKey(div)){
                    return count - where.get(div);
                }
                else{
                    where.put(div,count);
                }
            }
        }
    }
}
