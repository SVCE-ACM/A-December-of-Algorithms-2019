#include<iostream>
using namespace std;
main()
{
	 long long int n,temp;
	 int s1=0,s2=0;
	long long int r[1000],i=0;
	cin>>n;
	while(n>0)
	{
	r[i] = n%10;
	n = n/10;
	i++;
}

for(int j=0;j<i;j++)
{
	if(j%2==0)
	{
		s1 = s1+r[j];
	}
	if(j%2!=0)
	{
		temp = 2*r[j];
	while(temp>0)
	{
		s2 = s2+temp%10;
		temp = temp/10;
	}
	}
}
if((s1+s2)%10==0)
{
	for(int j=i-1;j>=0;j--)
	cout<<r[j];
	cout<<" passes the test";
}
else
{
	for(int j=i-1;j>=0;j--)
	cout<<r[j];
     cout<<" does not pass the test";
}
}
