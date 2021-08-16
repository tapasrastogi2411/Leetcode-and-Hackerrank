package Medium_Difficulty.Longest_Palindromic_String;

public class LongestPalindromicString {

    public boolean isPalindrome(String s){

        for (int i = 0; i < s.length() / 2; i ++){
            if (s.charAt(i) != s.charAt(s.length() - i - 1)){
                return false;
            }
        }
        return true;

    }
        public String longestPalindrome(String s) {
            
            if (s.length() < 2){
                return s;
            }
            
            if(s.length() == 2){
                if(isPalindrome(s)){
                    return s;
                }
                return s.substring(0, 1);
            }
    
            String result = "";
            for(int i = 0; i < s.length(); i++){
                for(int j = s.length() - 1; j > i; j--){
    
                    String substring = s.substring(i, j + 1);
    
                    if(isPalindrome(substring)){
                        if(substring.length() > result.length()){
                            result = substring;
                        }
                    }
                }
    
            }
            if(result.equals("")){
                return s.substring(0, 1);
            }
            return result;
      
        }

    public static void main(String[] args) {
        
        LongestPalindromicString instance = new LongestPalindromicString();
        String result = instance.longestPalindrome("cbbd");

        System.out.println(result);

    }

    
}