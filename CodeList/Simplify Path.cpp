/*
Simplify Path
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
*/
//用堆栈解决，遇到拿一个字符串记录两个'/'之间的内容（记得处理最后的一个字符串），然后遇到“..”就pop，不是就压入堆栈，记得排查乱七八糟的东西

class Solution {
public:
    string simplifyPath(string path) {
        stack<string> s;
	string str;
	
	for (int i=0;i<path.size();i++) {
		if(path[i]=='/'){
			if(str==".."){
				if(!s.empty())
				  s.pop();
			}
			else if (str!="."&&str!="") {
				s.push(str);
				
			}
			str="";
		}
		else{
			str+=path[i];
		}
		
	}
	 if (str == "..")//处理最后一截的字串
        {
            if (!s.empty())
               s.pop();
       }
        else if (str != "." && str != "")
            s.push(str);

     if(s.empty())
        
         return "/";

      string result;
      while (!s.empty()) {
	     result="/"+s.top()+result;
	     s.pop();
        }
      return result;

    }
};