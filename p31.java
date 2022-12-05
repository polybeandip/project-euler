//wasnt this problem on every contest ever?
import java.util.*;

public class p31 {

    public static void main(String[] args){
        List<Integer> l = new LinkedList(Arrays.asList(1,2,5,10,20,50,100,200));
        System.out.println(what(l,200));
    }

    //slow :\
    //works though
    private static int what(List<Integer> use, int target){
        if (target < 0){return 0;}
        if (target == 0){return 1;}

        int out= 0;
        int size= use.size();
        for (int i = size -1; i >= 0; i--){
            List<Integer> copy = new LinkedList<Integer>(use);
            out += what(copy, target - use.get(i));
            use.remove(i);
        }

        return out;
    }
}
