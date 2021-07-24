#include <stdio.h>
#include <stdlib.h>

int search(int *nums, int numsSize, int target){

    int left_index = 0;
    int right_index = numsSize - 1;

    while(left_index <= right_index){

        int middleIndex = (left_index + right_index) / 2;

        if(nums[middleIndex] == target){
            return middleIndex;
        }

        else if(nums[middleIndex] < target){
            left_index = middleIndex + 1; // Bringing left index towards the middle, searching on the left side
        }

        else {
            right_index = middleIndex - 1; // Searching on the right side instead
        }
    }
    
    // The number doesnt exist in the nums array
    return -1;

}

int main(){

    int input_array[] = {2, 0, 3, 5, 9, 12};
    int input_target = 91;

    printf("%d\n", search(input_array, input_target, 6));
}