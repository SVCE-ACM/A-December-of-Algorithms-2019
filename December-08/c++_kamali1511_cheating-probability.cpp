#include<iostream>
using namespace std;
int main()
{
	int i,j,r,c;
	double p[100][100];
	string a[100][100];
	float x = 0.0f;
	cin>>r;
	cin>>c;
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			cin>>a[i][j];
		}
	}
	
    for(i=0;i<r;i++)
    {
    	for(j=0;j<c;j++)
    	{
    		if(j>0)
    		{
    		if((a[i][j]==a[i][j+1])||(a[i][j]==a[i][j-1]))
    		p[i][j]+= 0.2;
		}
		else if(j<=0)
		{
			if(a[i][j]==a[i][j+1])
			p[i][j]+= 0.2;
		}
		if(a[i][j]==a[i+1][j])
		p[i][j]+= 0.2;
		
		if(i>0)
		{
			if(a[i][j]==a[i-1][j])
			p[i][j]+= 0.3;
		}
		if((i>0)&&(j>0))
		{
		if(a[i][j]==a[i+1][j+1]||a[i][j]==a[i-1][j-1]||a[i][j]==a[i+1][j-1]||a[i][j]==a[i-1][j+1])
		p[i][j]+= 0.025;
	}
	else if((i==0&&j==0))
	{
		if(a[i][j]==a[i+1][j+1])
		p[i][j]+= 0.025;
	}
	else if((i>0)&&(j<=0))
	{
		if(a[i][j]==a[i-1][j+1]||a[i][j]==a[i+1][j+1])
		p[i][j]+= 0.025;
	}
	else if((i<=0)&&(j>0))
	{
		if(a[i][j]==a[i+1][j-1]||a[i][j]==a[i+1][j+1])
		p[i][j]+= 0.025;
	}
	else
	{
	p[i][j]=x;
	}
    	
}
}
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			if(p[i][j]==x)
			{
				cout<<"0.0"<<" ";
			}
			else
			cout<<p[i][j]<<" ";
		}
		cout<<"\n";
	}
	return 0;
}
