/*Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

选一个hash表，其实就是通过字符表达的值作为index能找到其在string中位置的储存结构，然后从左往右扫描一遍，准备一个start指针，凡是找到一个重复的字符，那么先算一下是不是当时情况下的最长，然后更新最长值，接着把之前的start到被重复的字符的hash值重新设置为-1，然后把当前的hash值更新

*/

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
    int hash[256];
    for (int i=0; i<256; i++) {
        hash[i]=-1;
    }
    
    int start = 0, res = 0;
    
    int i;
    for (i=0; i<s.length(); i++) {
        if(hash[s[i]]!=-1){
            if (res<i-start) {
                res = i - start;
            }
            
            for (int j=start; j<hash[s[i]]; j++) {
                hash[j]=-1;
            }
            if(hash[  s[i] ] + 1  > start ){
                start = hash[ s[i] ] +1;
            }
        }
        hash[s[i]]=i;
    }
    if(res<i-start) res=i-start;
    return res;
    }
};