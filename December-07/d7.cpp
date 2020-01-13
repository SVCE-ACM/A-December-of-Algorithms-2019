#include<iostream>
#include<queue>

using namespace std;

class Person {
    public:
    int no;
    char id;
    void get() {
        cout<<"\nEnter the token number & id:"<<endl;
        cin>>no>>id;
    }
    void print() {
        cout<<"\n("<<no<<","<<id<<")"<<endl;
    }
};

int main() {
    int n;
    cout<<"\nEnter the # of patients:";
    cin>>n;
    queue<Person> ppl,tmp;
    for(int i = 0; i < n; i++) {
        Person tmp;
        tmp.get();
        ppl.push(tmp);
    }
    char k;
    cout<<"\nEnter the id of k:";
    cin>>k;
    while(!ppl.empty()) {
        Person top = ppl.front();
        if(top.id == k) {
            ppl.pop();
            top.print();
            while(!tmp.empty()) {
                tmp.front().print();
                tmp.pop();
            }
        } else {
            tmp.push(top);
            ppl.pop();
        }
    }
    while(!tmp.empty()) {
        tmp.front().print();
        tmp.pop();
    }
}