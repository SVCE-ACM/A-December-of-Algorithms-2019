/*
Started On : December 1, 2019
Author : Nilesh D
Objective : Performed a Queued Up Operation
*/

# include <iostream>
# include <queue>
# include <utility>
using namespace std;

int main(void)
{
  int n;
  cout << "\nEnter N: ";
  cin >> n;
  queue < pair<int, char> > Q;
  cout << "Enter (token no, id): ";
  while(n--)
  {
    int token_no;
    char id;
    cin >> token_no >> id;
    Q.push(make_pair(token_no, id));
  }
  int k;
  cout << "Enter k: ";
  cin >> k;
  queue < pair<int, char> > tempQ;
  while(--k)
  {
    tempQ.push(Q.front());
    Q.pop();
  }
  
  pair <int, char> bribe = Q.front();
  Q.pop();
  
  while(!Q.empty())
  {
    tempQ.push(Q.front());
    Q.pop();
  }
  Q.push(bribe);
  
  while(!tempQ.empty())
  {
    Q.push(tempQ.front());
    tempQ.pop();
  }
  
  while(!Q.empty())
  {
    cout << "(" << Q.front().first << ", " << Q.front().second << ")" << '\n';
    Q.pop();
  }
  return 0;
}
