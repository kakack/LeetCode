
/*Count and Say 
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

*/
class Solution {
public:
   string getNext(const string &s){
       stringstream ss;
       
       for(auto i=s.begin();i!=s.end();){
           auto j =find_if(i,s.end(),bind1st(not_equal_to<char>(), *i));//巧妙使用STL，这两个方法怎么用的看笔记
           ss<<distance(i,j) <<*i;
           i=j;
       }
       return ss.str();
   }


    string countAndSay(int n) {
        string s("1");
        
        while(--n)
           s = getNext(s);
           
        return s;
    }
};