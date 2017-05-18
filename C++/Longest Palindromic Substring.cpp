/*Longest Palindromic Substring
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

第一个方法是稍微暴力一点的，每次遍历的时候从某元素中间向两边走，判断并记录最长回文子串，切记可能出现ABCBA和ABCCBA两种类型的回文

第二个属于manchester算法
*/

class Solution {
public:
    string longestPalindrome(string s) {
        
        const int len=s.size();
         if(len<=1) return s;
         
         int max=0,tmp_len=0;
         string tmp,res;
         
         for(int i=0;i<len;i++){
             
             tmp.insert(tmp.begin(),s[i]);
             for(int j=1;(i-j>=0)&&(i+j<len);j++){
                 
                 if(s[i-j]!=s[i+j])
                   break;
                   
                 tmp.insert(tmp.begin(),s[i-j]);
                 tmp.insert(tmp.end(),s[i+j]);
                 tmp_len=j*2+1; 
             }
             
             if(tmp_len>=max){
                res=tmp;
                max=tmp_len;
             }
            tmp="";
            tmp_len=0;
                
            for(int j = 0; (i - j >= 0) && (i + j + 1 < len); j++){
                if (s[i - j] != s[i + j + 1])
                  break;
                tmp.insert(tmp.begin(),s[i-j]);
                tmp.insert(tmp.end(),s[i+j+1]);
                tmp_len=j*2+2; 
            }
            
            if(tmp_len>=max){
                res=tmp;
                max=tmp_len;
             }
             
             tmp="";
             tmp_len=0;
         }
        
        return res;
    }
};