public class p35{
    public static void main(String[] args){
        int count =0;
        outer:
        for (int i = 2; i <= 1000000; i++){
            for (int num : circle(i)){
                if(!isPrime(num)){continue outer;}
            }
            count++;
        }
        System.out.println(count);
    }

    private static boolean isPrime(int n){
        for (int i = 2; i <= Math.sqrt(n); i++){
            if (n % i == 0){return false;}
        }

        return true;
    }

    private static int[] circle(int n){
        StringBuilder nAsString = new StringBuilder(Integer.valueOf(n).toString());
        int size = nAsString.length();
        int[] circles = new int[size];

        for (int i = 0; i < size; i++){
            char digit = nAsString.charAt(0);
            nAsString.delete(0,1);
            nAsString.append(digit);
            circles[i] = Integer.valueOf(nAsString.toString());
        }

        return circles;
        
    }
}