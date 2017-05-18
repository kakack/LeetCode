//Majority Element 

//Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.某处看到最好的办法其实是遍历一遍，如果有不同的则把两个都删去，剩下的就是需要的

You may assume that the array is non-empty and the majority element always exist in the array.

class Solution {
public:
    int majorityElement(vector<int> &num) {
        map<int, int> m;
        for(int i=0;i<num.size();i++){
            if(m.find(num[i])!=m.end())
               m[num[i]]++;
            else
              m[num[i]] = 1;
        
            if(m[num[i]]>num.size()/2)
              return num[i];
        }
    }
};