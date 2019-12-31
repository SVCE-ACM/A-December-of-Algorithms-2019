#include<iostream> 
#define ROW 1000 
#define COL 1000
using namespace std; 

void spiral(int m, int n, int a[ROW][COL]) 
{ 
    int i, k = 0, l = 0; 
    while (k < m && l < n) { 
        for (i = l; i < n; ++i)
            cout << a[k][i] << " "; 
        k++; 
        for (i = k; i < m; ++i)
            cout << a[i][n - 1] << " "; 
        n--; 
        if (k < m) { 
            for (i = n - 1; i >= l; --i)
                cout << a[m - 1][i] << " "; 
            m--; 
        } 
        if (l < n) { 
            for (i = m - 1; i >= k; --i)
                cout << a[i][l] << " "; 
            l++; 
        } 
    } 
} 
int main() 
{ 
    int a[ROW][COL],r,c;
    cout<<"\nEnter # of row & col:";
    cin>>r>>c;
    cout<<"\n--Enter the matrix--\n";
    for(int i=0;i<r;i++)
        for(int j=0;j<c;j++)
            cin>>a[i][j];
    spiral(r,c,a); 
    return 0; 
} 