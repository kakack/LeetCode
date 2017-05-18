
//Palindrome Number 
//Determine whether an integer is a palindrome. Do this without extra space.
//转换成string之后好做一点


class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0)
          return false;
        string tmp = toString(x);
        return isPalindrome(tmp);
    }
    
    string toString(int x){
        string res;
        while(x>0){
            res.insert(res.begin(), '0'+x%10);
            x=x/10;
        } 
        return res;
    }
    
    bool isPalindrome(string x){
        int i=0, j=x.size()-1;
        while(i<=j){
            if(x[i]!=x[j])
              return false;
            else{
                i++;
                j--;
            }
        }
        return true;
    }
};