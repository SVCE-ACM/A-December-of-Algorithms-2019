#include<iostream>
using namespace std;

int cookie_count(int n,int p,int c) {
    int cookies = 0,freeCookies = 0,remaining = 0;
    cookies += n/p;
    freeCookies = cookies/c;
    remaining = cookies%c;
    do {
        cookies += freeCookies;
        int tmp = freeCookies;
        freeCookies /= c;
        remaining += tmp%c;
    } while(freeCookies > 0);
    cookies += remaining / c;
    return cookies;
}

int main() {
    int n,p,c;
    cout<<"\nEnter the total cost:";
    cin>>n;
    cout<<"\nEnter the cost of a cookie:";
    cin>>p;
    cout<<"\nEnter # of jar required for a cookie:";
    cin>>c;
    cout<<endl<<cookie_count(n,p,c);
    return 0;
}