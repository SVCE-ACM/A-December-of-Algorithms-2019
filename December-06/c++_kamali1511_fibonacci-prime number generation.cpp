#include<iostream>
using namespace std;    
int main()    
{    
int n1=1,n2=1,n3,i,n,j;
cout<<"Enter the value for (n): ";    
cin>>n; 
cout<<"Generated Fibonacci Prime Number Generation upto ("<<n<<") :"<<endl;
 for(i=0;i<n;)   
 {    
  n3=n1+n2;    
   bool flag = true;

   for(int j = 2; j <= n3 / 2; j++) {
      if(n3 % j == 0) {
         flag = false;
         break;
      }
   }
   if (flag==true)
   {
   	 i++;
      cout<<n3<<" ";
  }
  n1=n2;    
  n2=n3;    
 }  
 return 0;
}
