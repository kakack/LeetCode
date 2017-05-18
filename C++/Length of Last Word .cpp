/*
Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
逻辑上从前往后扫描简单一点，但是我不想做很多无用计算，就从后往前扫了，所以会有很多细节要考虑
*/

class Solution {
public:
    int lengthOfLastWord(const char *s) {
        int len=strlen(s);
        
        
        while(len>=0&&s[len-1]==' ')
          len--;
        if(len<=0)
          return 0; 
          
          
        int i=1;
        
        char c=s[len-i];
        for(;i<=len&&c!=' ';i++){
            c=s[len-i];
        }
        
        if(c==' ')
         return i-2;
        else
         return i-1;
          
        
    }
};