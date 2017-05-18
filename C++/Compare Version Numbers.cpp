/*Compare Version Numbers
优化成x.y形式，x前方没0
找.
比较.前面部分
如果一样，后面重新比一遍

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
*/

class Solution {
public:
    int findPoint(string s){
        for(int i=0;i<s.length();i++)
           if(s[i]=='.')
             return i;
        return s.length();
    }
    
    bool compare(string s1, string s2){
        if(s1.length()>s2.length())
          return true;
        else if(s1.length()<s2.length())
          return false;
        else{
            for(int i=0;i<s1.length();i++)
               if(s1[i]>s2[i])
                 return true;
               else if(s1[i]<s2[i])
                 return false;
        }
        return true;
    }
    
    int compareVersion(string version1, string version2) {
        if(findPoint(version1)==version1.length())
           version1 = version1 + ".0";
        if(findPoint(version2)==version2.length())
           version2 = version2 + ".0";
        while(version1[0]=='0' && version1[1]!='.') 
			version1 = version1.substr(1,version1.length()-1);
        while(version2[0]=='0' && version2[1]!='.') 
			version2 = version2.substr(1,version2.length()-1);  

        if(version1 == version2)
          return 0;

        string forward1 = version1.substr(0, findPoint(version1));
        string back1 = version1.substr(findPoint(version1)+1, version1.length()-findPoint(version1)-1);
        string forward2 = version2.substr(0, findPoint(version2));
        string back2 = version2.substr(findPoint(version2)+1, version2.length()-findPoint(version2)-1);
        
        if(forward1 != forward2){
            //compare forward
            return compare(forward1,forward2)?1:-1;
            
        }
        else{
            //compare back
            return compareVersion(back1,back2);
        }
        
    }
};