
/*Implement strStr()
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Update (2014-11-02):
The signature of the function had been updated to return the index instead of the pointer. If you still see your function signature returns a char * or String, please click the reload button  to reset your code definition.

准备了四个指针
*/
class Solution {
public:
    int strStr(char *haystack, char *needle) {
        
        if(!*needle) return 0;
        
        char *p1;//在haystack里遍历用
        char *p2;//在needle中遍历用
        char *p1_a = haystack;//在haystack里，找向可能存在比较的最后一个字符
        
        for(p2=&needle[1];*p2;p2++)
            p1_a ++;
            
        for(p1=haystack;*p1_a;p1_a++){
            char *p1_old = (char*) p1;//记录好开始比较的第一个字符
            p2=needle;
            while (*p1&&*p2&&*p1==*p2){
                p1++;
                p2++;
            }
            
            if(!*p2) return p1_old-haystack;
            
            p1=p1_old+1;
            
        }
        
        return -1;
        
        
    }
};