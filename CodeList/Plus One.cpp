
/*
Plus One 

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
*/
class Solution {
public:
    vector<int> plusOne(vector<int> &digits) {
       	int n=digits.size()-1;
			
			digits[n]+=1;
			
			while(digits[n]>=10&&n>0){
				digits[n]=digits[n]%10;
				  digits[n-1]+=1;
				  n--;
			}
			
			if(digits[0]>=10){
				digits[0]=digits[0]%10;
				digits.insert(digits.begin(),1);
				
			}
        return digits;
        
    }
};