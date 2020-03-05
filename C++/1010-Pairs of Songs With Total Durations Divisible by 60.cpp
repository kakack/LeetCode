#include <vector>
#include <iostream>
class Solution
{
public:
    int numPairsDivisibleBy60(vector<int> &time)
    {
        int res = 0;
        vector<int> store(60); 
        for(auto iter = time.begin(); iter != time.end(); iter ++){
            store[*iter % 60] ++;
        }
        res += store[0] * (store[0] - 1) / 2 + store[30] * (store[30] - 1) / 2;
        for(int i = 1; i < 30; i++){
            res += store[i] * store[60 -i];
        }
        return res;
    }
};

// int main(int argc, char const *argv[])
// {
//     Solution s = Solution.__init__();
//     vector<int> time = []
//     return 0;
// }