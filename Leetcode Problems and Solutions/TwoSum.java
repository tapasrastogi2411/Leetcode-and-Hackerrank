import java.util.HashMap;
import java.util.*;
/**
 * TwoSum
 */
public class TwoSum {

    public static int[] twoSum(int [] array, int target){

        HashMap<Integer, Integer> differenceMap = new HashMap<>();

        for(int i = 0; i < array.length; i++){

            if (!differenceMap.containsKey(array[i])){

                int difference = target - array[i];
                differenceMap.put(difference, i);

            }
            else {
                return new int[]{differenceMap.get(array[i]), i};
            }
        }
        return null;

    }

    public static void main(String[] args) {

        int [] inputList = {2, 5,  2};
        int inputTarget = 4;
        int [] outputList;
        outputList = twoSum(inputList, inputTarget);
        System.out.println(Arrays.toString(outputList));
    }
}