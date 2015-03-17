
/*Permutations II 

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
*/

class Solution {
public:
    vector<vector<int> > permuteUnique(vector<int> &num) {
        vector<vector<int> > result;
        unordered_map<int, int> exist;
        
        if(num.size() == 0)
          return result;
        
        if(num.size() == 1){
            
            result.push_back(num);
            return result;
        }
        
        
        //DFS
        
        int length = num.size();
        
        for(int i=length-1;i>=0;i--){
            vector<vector<int> > nextPer;
            vector<int> temp(num);
            int curNum = num[i];
            if(exist.find(curNum) != exist.end()) {
                continue;
            }
            
            else {
                exist[curNum] = 1;
            }
            
            temp.erase(temp.begin() + i);
            nextPer = permuteUnique(temp);//这条好屌, 从temp中获取所有不重复的permution
            for(int j = 0;j<nextPer.size();j++){
                nextPer[j].push_back(curNum);
                vector<int> temp_result = nextPer[j];
                result.push_back(temp_result);
            }
         }
         
         return result;
    }
};