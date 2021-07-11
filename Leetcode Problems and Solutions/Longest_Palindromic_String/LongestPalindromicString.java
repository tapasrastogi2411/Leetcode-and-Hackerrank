import java.util.HashMap;

/**
 * LongestPalindromicString
 */
public class LongestPalindromicString {

    public char longestPalindromicString(String s){
        
        int [] myArray = {10, 20, 30};
        for(int i = 0; i < myArray.length; i++){

            System.out.println(myArray[i]);
        }

        HashMap<String, String> myHashMap = new HashMap<>();
        myHashMap.put("Tapas", "Rastogi");
        myHashMap.put("Roger", "Federer");

        System.out.println(myHashMap);
        System.out.println("The meaning of life is: " + myHashMap.containsKey("Tapas"));

        return 'c';

    }

    public static void main(String[] args) {
        
        LongestPalindromicString instance = new LongestPalindromicString();
        instance.longestPalindromicString("Hello World");
    }

    
}