/*Permutation Sequence
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

不要想用上一题的next_Permutation来做
思路是康托编码
微软今年的笔试题里有一道类似的，我之前已经提到过了，是只有0和1的字符串，求第k个排列是什么样子的。这道题比那个要难一些，但是总体的思路是一样的。假设有n个数要组成排列，求第k个排列。像填表一样，从高位往地位，逐个填写。先考虑有n-1个数要组成排列，最多有（n-1)!种情况，当第n个数加入后，第n个数可以是从1增加到n的，没增加1，所包含的全排列数就会增加（n-1)!，因此，如果用k/（n-1）!，得到的就是第高位排列应该出现的数字。为了计算后面的位应该填什么，k要更新为k%(n-1)!。计算第i位应该填的是k/(i-1)!。不，不仅仅是这样，这里应该是这道题和01串那道题一个很大的不同之处，在填第i位的时候，还要看剩下了哪些数字，应该在剩下的那些数字里找第k/(i-1)!个。

代码里为什么要先对k减1，用简单的例子就能理解。就像在一个矩阵中，给了矩阵中的第k个数，要求它对应矩阵中的那个位置，也会先对他减一的。题目中给出了所参与排列数的取值范围，因此可以先把阶乘算出来，放到数组里。
*/

class Solution {
public:
    const int fac[10] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};///阶乘  
    
    string getPermutation(int n, int k) {
        string res(n,'0');
        
        bool vis[10];
        k--;
        for (int i = n-1; i >= 0; i--){
            int temp=k/fac[i];
            int j=1;
            for(;j<10;j++){
                if(vis[j] == 0)
                    temp--;
                if(temp<0)
                    break;
            }
            res[n-i-1] = '0'+j;
            vis[j] = 1;
            k%=fac[i];
            
        }
        return res;
         
    }
};