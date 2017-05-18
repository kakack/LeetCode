/*Word Ladder 
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.

广度搜索，
*/

class Solution {
public:
    int ladderLength(string start, string end, unordered_set<string> &dict) {
        if(start.size() == 0 || end.size() == 0 || start.size() != end.size())
          return 0;
          
         queue<string> next, current; // 当前层，下一层
         unordered_set<string> visited; // 判重
         
        // unordered_map<string, string > father;//我也不知道这货拿来搞毛用
         
         int level = 0; // 层次 
         bool found = false;
         
         current.push(start);
         
         while(!current.empty()&&!found){
             
             level++;
             
             while (!current.empty() && !found) { 
                 const string str(current.front()); 
                 current.pop();
             
                 for(size_t i=0;i<str.size();i++){
                     string new_word(str);
                     for (char c = 'a'; c <= 'z'; c++) { 
                         if (c == new_word[i]) 
                            continue;
                         
                         swap(c, new_word[i]); 
                         
                         if (new_word == end) { 
                             found = true; //找到了 
                         //    father[new_word] = str; 
                             break;
                         }//如果一下子就找到了
                         
                         if (dict.count(new_word) > 0 && !visited.count(new_word)) {
                             next.push(new_word); 
                             visited.insert(new_word); 
                       //      father[new_word] = str;      
                         }//如果之前没访问过这个词，而且dict里有这货
                         //如果不在dict里面就不要管它了
                         swap(c, new_word[i]); // 恢复该单词 
                     }
                 }
             } 
             swap(next, current); //!!! 交换两个队列
         }
         if (found) return level+1;
            else return 0;
    	
    }
};