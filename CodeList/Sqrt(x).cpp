/*
Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.

后来懒惰啊我兄说这个题直接用二分查找就行，那就比较简单，连牛顿算法都用不上了，
基本上如果要ac的话，写死100次循环足够应付所有int了
*/

class Solution {
public:
    int sqrt(int x) {
        double y=(double)x;
        if(x==0)
         return 0;
         
        else{
        
            for(int i=0;i<100;i++){
                y=(y+x/y)/2;
            }
        }
        
        return int(y);
             
    }
};

//这个说我超时了，但是我本地跑出来结果是一样的

//class Solution {
//public:
//    int sqrt(int x) {
//        
//    if(x==1)
//     return 1;
//
//	long floor=0;
//	long ceil=(long)x;
//	long mid=(long)x/2;
//	       
//	while(true){
//	           
//	   if(mid*mid==x||(mid*mid<x&&(mid+1)*(mid+1)>x))
//	      break;
//	   
//	   else if(mid*mid<x){
//	      floor=mid;
//	      mid=(ceil+floor)/2;
//	   }
//	           
//	   else {
//	      ceil=mid;
//	      mid=(ceil+floor)/2;
//	           }
//	       }
//       
//       return mid;
//        
//    }
//};