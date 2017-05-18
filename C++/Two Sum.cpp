/*
Two Sum
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
 hash
从左往右扫描一遍，然后将数及坐标，存到map中。然后再扫描一遍即可。时间复杂度O(n)，我忘记了这题哪家实习面试的时候问过我，当时答的跟屎一样，道理是充分利用map访问快的又是，搜寻两边就行，
*/

class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        map<int, int> mapping;  
        vector<int> result;
        
        for(int i=0;i<numbers.size();i++){
            mapping[numbers[i]] = i;
        }
        
        for(int i=0;i<numbers.size();i++){
            int searched = target-numbers[i];
            if(mapping.find(searched)!=mapping.end()&&i!=mapping[searched]){//这边注意有一个case是[3,1,2,4], 6。不能给人弄出俩1来
                result.push_back(i+1);
                result.push_back(mapping[searched]+1);
                break;
            }
        }
        
        return result;
    }
};