/*
Regular Expression Matching

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true


*/
//递归法，每次都看p的下一个字符是不是*
class Solution {
public:
    bool isMatch(const char *s, const char *p) {
        if(*p=='\0') return *s=='\0';
        
        //如果*p的下一个不是‘*’，那么必须符合
        
        if(*(p+1)!='*'){
          if(*p==*s||(*p=='.'&&*s!='\0'))//那么只要当前这个满足，就可以暂定认为是满足的，继续往下一个去比较
             return isMatch(s+1,p+1);
          else
             return false;
        }
        //否则*p的下一个是*
        else{
            while(*p==*s||(*p=='.'&&*s!='\0')){//当前这个满足就可以往后面跳两个
                if(isMatch(s,p+2))
                   return true;
                s++;
            }
            return isMatch(s,p+2);
        }
    }
};