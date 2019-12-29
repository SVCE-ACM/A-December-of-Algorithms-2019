#include <iostream>
#include <conio.h>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

struct n 
{
  int priority,token;
  char info;
  struct n *next;
};
class Priority_Queue
{
private:
  n *f;

public:
  Priority_Queue()
  {

    f = NULL;
  }
  void insert(int p,int tn, char i)
  {
    n *t, *q;
    t = new n;
    t->info = i;
    t->priority = p;
    t->token = tn;
    if (f == NULL || p < f->priority)
    {
      t->next = f;
      f = t;
    }
    else
    {
      q = f;
      while (q->next != NULL && q->next->priority <= p)
        q = q->next;
      t->next = q->next;
      q->next = t;
    }
  }
  
  void get()
  {	int n,t[100];
  char id[100],k;
  cout<<"Enter N: ";
  cin>>n;
  cout<<"Enter (token no, id): "<<endl;
  for(int j=0;j<n;j++)
  cin>>t[j]>>id[j];
  cout<<"Enter k: ";
  cin>>k;
  for(int j=0;j<n;j++)
  {
  	static int l=2;
  	if(k!=id[j])
  	{
  insert(l,t[j],id[j]);
  l++;
}
else
insert(1,t[j],id[j]);
}

  }
  
  void show()
  {
  	n *ptr;
    ptr = f;
    if (f == NULL)
      cout << "Queue is empty\n";
    else
    {
      while (ptr != NULL)
      {
        cout <<"("<< ptr->token<<"," << " " << ptr->info<<")" << endl;
        ptr = ptr->next;
        
      }
    }
  }
  
 
  
};
int main()
{
	 Priority_Queue pq;
	 pq.get();
  cout<<"The order is:"<<endl;
pq.show();
 return 0;
}


 

