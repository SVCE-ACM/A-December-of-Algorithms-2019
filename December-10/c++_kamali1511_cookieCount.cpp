#include<iostream>
using namespace std;

int cookieCount(int n,int p,int c)
{
	int cookies = 0; int jar = 0;
	cookies = n/p;
	jar = cookies;
	while(jar >= c){
		cookies += jar / c;
		jar = jar % c + jar / c;
	}
	
	return cookies;		
}
main()
{
int c= cookieCount(12,4,4);
cout<<c;
	
}
