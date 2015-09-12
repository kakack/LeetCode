/*Multiply Strings
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
*/

class Solution {
public:
    
string add(string a, string b){
	string res;
	
	if(a.length()==0&&b.length()==0)
	   return "0";
	if(a.length()<b.length()){
		string tmp=a;
		a=b;
		b=tmp;
	}
		int len=a.length()-b.length();
		for(;len>0;len--)
		  b = '0'+b;
	
	
	int carry = 0;
	for (int i=a.length()-1;i>=0;i--) {
		int tmp = (a[i]-'0') + (b[i]-'0') + carry;
		if(tmp>=10){
			tmp-=10;
			carry=1; 
		}
		else{
			tmp =tmp;
			carry=0;
		}
		char tmp_c = '0'+tmp;
		res = tmp_c+res;
	}
	if(carry==1)
	   return '1'+res;
	else
	   return res;
	
}


string multi_single(string a, char b){
	int b_i = b-'0',carry = 0;
	string res;
	
	for (int i=a.length()-1;i>=0;i--) {
		int tmp = (b_i*(a[i]-'0')+carry)%10;
		carry = (b_i*(a[i]-'0')+carry)/10;
		char tmp_c = '0'+tmp;
		res = tmp_c+res;
	}
	if(carry>0){
		char carry_c = carry+'0';
		return carry_c+res;
	}
	   
	else
	   return res;
}

    string multiply(string num1, string num2) {
     string res;
     	
	if(num1=="0"||num2=="0")
	  return "0";
	  
	int count = 0;
	for (int i=num2.length()-1;i>=0;i--) {
		
		string tmp_res = multi_single(num1, num2[i]);
		int tmp_c = count;
		while (tmp_c--) {
			tmp_res = tmp_res + '0';
		}
		count++;
		res = add(res,tmp_res);
	}
	
	return res;   
    }
};