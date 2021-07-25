#include <stdio.h>
#include <stdlib.h>


int maxProfit(int* prices, int pricesSize){

    int max_profit = 0;

    for(int i = 0; i < pricesSize - 1; i++){

        for(int j = i + 1; j < pricesSize; j++){

            int profit = prices[j] - prices[i];

            if(profit > max_profit){
                max_profit = profit;
            } 
        }
    }

    return max_profit;
    
}

int main(){

    int input_list[] = {7,6,4,3,1};
    
    printf("%d\n", maxProfit(input_list, 5));

    return 0;

}