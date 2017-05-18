/*Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

思路不同于最暴力的O(n^2)解法，这边从左往右先存下最小值的index，然后先存好已有的max，再往右遍历，找到更大的max值就更新
*/

class Solution {
public:
    int maxProfit(vector<int> &prices) {
        
        int n=prices.size();
        int diff,max=0,min=0;
        
        
        for(int i=0;i<n;i++){
            
            if(prices[i]<prices[min])
               min=i;
               
            if(prices[i]-prices[min]>max)
              max=prices[i]-prices[min];
 
        }
        return max;
        
    }
};