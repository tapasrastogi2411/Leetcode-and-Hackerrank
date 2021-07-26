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

int maxProfitVersion2(int *prices, int pricesSize){

    int max_profit = 0;
    int buy_price_to_consider = prices[0];

    if (pricesSize < 2){
        return 0;
    }
    for (int i = 1; i < pricesSize; i++){
        if(prices[i] < buy_price_to_consider){
            buy_price_to_consider = prices[i];
        }
        else if(prices[i] > buy_price_to_consider){
            int profit = prices[i] - buy_price_to_consider;
            if(profit > max_profit){
                max_profit = profit;
            }
        }
        

        
    }
    return max_profit;
}

int main(){

    int input_list[] = {7, 1, 5, 3, 6, 4};
    
    printf("%d\n", maxProfitVersion2(input_list, 6));

    return 0;

}