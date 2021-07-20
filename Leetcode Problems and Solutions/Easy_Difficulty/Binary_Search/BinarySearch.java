/* Link to problem: https://leetcode.com/problems/binary-search/
Difficulty: Easy

Leetcode Problem no 704: Binary Search - Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
*/

package Easy_Difficulty.Binary_Search;

public class BinarySearch {
    
    public int performBinarySearch(int [] nums, int target){

        int rightIndex = nums.length - 1;
        int leftIndex = 0;

        while (leftIndex <= rightIndex) {

            int middleIndex = (leftIndex + rightIndex) / 2;
            
            if (nums[middleIndex] == target) {
                return middleIndex;
                
            } else if (nums[middleIndex] < target) {
                leftIndex = middleIndex - 1;
                
            } else {
                rightIndex = middleIndex + 1;
            }

        }
        return -1;
    }

    

public static void main(String[] args) {

    System.out.println("There will be a day");
    
}

}
