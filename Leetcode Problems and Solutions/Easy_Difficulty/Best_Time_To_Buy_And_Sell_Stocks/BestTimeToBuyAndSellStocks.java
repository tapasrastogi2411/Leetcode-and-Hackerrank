package Easy_Difficulty.Best_Time_To_Buy_And_Sell_Stocks;

public class BestTimeToBuyAndSellStocks {

    public int maxProfit(int prices[]){

        int maximumProfit = 0;
        int buyPriceToConsider = prices[0];

        if(prices.length < 2){
            return 0;
        }

        for(int i = 1; i < prices.length; i++){

            if(prices[i] < buyPriceToConsider){
                buyPriceToConsider = prices[i];
            }

            else {
                int profit = prices[i] - buyPriceToConsider;
                if(profit > maximumProfit){
                    maximumProfit = profit;
                }
            }
        }

        return maximumProfit;
    }

    public static void main(String[] args) {

        int[] inputList = {7, 1, 5, 3, 6 ,4};

        BestTimeToBuyAndSellStocks bestTimeToBuyAndSellStocks = new BestTimeToBuyAndSellStocks();

        int result = bestTimeToBuyAndSellStocks.maxProfit(inputList);

        System.out.println(result);
    }
    
}
