/*

Best Time to Buy and Sell Stock II
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

*/

class Solution {
public:
    int maxProfit(vector<int> &prices) {
        
        int profile=0,n=prices.size(),sell,buy;
        
        if(n==0||n==1)
          return 0;
          
        if(prices[1]>=prices[0])
           buy=0;
        
        for(int i=1;i<n;i++){
            if(prices[i+1]>=prices[i]&&prices[i-1]>=prices[i])
              buy=i;
              
            else if((prices[i+1]<=prices[i]&&prices[i-1]<prices[i])||(prices[i-1]<prices[i]&&i==n-1)){
                sell=i;
                profile+=prices[sell]-prices[buy];
                
            }
        }
        
        return profile;
        
        
    }
};