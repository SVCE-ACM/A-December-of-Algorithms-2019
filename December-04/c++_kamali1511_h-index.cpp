#include<iostream>
#include<vector>
#include<stdlib.h>
using namespace std;
 class Solution {
public:
    int hIndex(vector<int>& citations) {
        vector<int> p(citations.size()+1,0);
        for(int i = 0; i < citations.size(); i++){
            if(citations[i] > citations.size()){
                p[citations.size()]++;
            }
            else p[citations[i]]++;
        }
        for(int j = p.size()-1; j >= 1; j--){
            p[j-1] += p[j];
            if(p[j] >= j) return j;
        }
        return 0;
    }
};
int main()
{
	Solution s;
	vector<int> v;
	int n,a[1000];
	cout<<"Enter N: ";
	cin>>n;
	cout<<"Enter the citations: "<<endl;
	for(int i=0;i<n;i++)
	{
		cin>>a[i];
		v.push_back(a[i]);
	}
	int x= s.hIndex(v);
	cout<<"The h-index is: "<<x;
	
}
