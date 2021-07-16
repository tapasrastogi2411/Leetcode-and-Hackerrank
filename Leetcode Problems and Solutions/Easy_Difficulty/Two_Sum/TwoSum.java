package Easy_Difficulty.Two_Sum;

/*

Link to Problem: https://leetcode.com/problems/two-sum/
Difficulty - Easy

Leetcode Problem number 1: Two Sum - Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

*/

import java.util.HashMap;
import java.util.*;

public class TwoSum {

    public static int[] twoSum(int [] array, int target){
        
        // Initialising the HashMap data structure to use from java.utils library
        HashMap<Integer, Integer> differenceMap = new HashMap<>();

        // Looping through all the elements in the input array and seeing if it is there in the difference hashmap
        for(int i = 0; i < array.length; i++){

            if (!differenceMap.containsKey(array[i])){
                
                // We build the difference hashmap here 
                int difference = target - array[i];
                differenceMap.put(difference, i);

            }
            else {
                
                // We return the corresponding indices as required
                return new int[]{differenceMap.get(array[i]), i};
            }
        }
        return null;

    }

    // Testing out the method here in the main method
    public static void main(String[] args) {

        int [] inputList = {2, 5,  2};
        int inputTarget = 4;
        int [] outputList;
        outputList = twoSum(inputList, inputTarget);
        System.out.println(Arrays.toString(outputList));
    }
}