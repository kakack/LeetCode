/*
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
*/

//O(N^2)的解法，完全模拟
//class Solution {
//public:
//    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
//        
//        int N = gas.size();
//        int index;
//        
//        for(int i = 0; i < N; i++){
//            
//            int sum = 0;
//            
//            for(int j = 0; j < N; j++){
//                
//                index = (i+j)%N;
//                sum=sum+gas[index]-cost[index];
//                
//                if(sum<0)
//                  break;
//                  
//                if(j==N)
//                  return 1;
//            }
//
//        }
//        
//        return -1;
//        
//    }
//};



/*
O(N)的解法只要完整的过一遍循环即可，因为如果不能跑完，一定是总的cost和大于gas的和，接下来只要是确定起点下标即可
*/
class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        
        int j = -1;
        int total = 0;
        for(int i = 0, sum = 0; i < gas.size(); i++){
            sum+=gas[i]-cost[i];
            total+=gas[i]-cost[i];
            
            if(sum<0){
                j = i;
                sum = 0;
            }
        }
        
        return total>=0? j+1 : -1;

    }
};