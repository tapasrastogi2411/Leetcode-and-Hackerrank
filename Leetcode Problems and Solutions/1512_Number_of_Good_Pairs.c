#include <stdio.h>
#include <stdlib.h>

int numIdenticalPairs(int* nums, int numsSize){

    int pair_counter = 0;
    for(int i = 0; i < numsSize; i++){
        
        int number_to_check = nums[i];
        
        for(int j = 1; j < numsSize; j++){
            
            if((number_to_check == nums[j]) && i < j){
                pair_counter++;
            }
        }
    }
    return pair_counter;

}

int main(){

    int input_nums[] = {1, 2, 3, 1, 1, 3};
    int output_recived;

    output_recived = numIdenticalPairs(input_nums, 6);
    printf("%d\n", output_recived);

}