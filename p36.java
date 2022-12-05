public class p36 {
    public static void main(String[] args){
        int sum = 0;
        for (int i = 1; i <= 1000000; i++){
            String decimal = ((Integer)  i).toString();
            String binary = Integer.toBinaryString(i);
            if (isPalindrome(decimal) && isPalindrome(binary)){sum+= i;}
        }

        System.out.println(sum);
    }

    private static boolean isPalindrome(String s){
        int n = s.length();
        //include this line numbers with zeros at the end are palindromic
        //if(s.charAt(n-1) == '0'){return isPalindrome(s.substring(0,n-1));}
        for (int i = 0; i < n/2; i++){
            if (s.charAt(i) != s.charAt(n-1-i)){return false;}
        }

        return true;
    }

}
