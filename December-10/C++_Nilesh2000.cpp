// Author : Nilesh D
// December 10 - Count The Cookies

#include <iostream>

using namespace std;

int cookieCount(int n, int p, int c)
{
  int Total, Jars;
  Total = Jars = n / p;
  while (Jars >= c)
  {
    Total += Jars / c;
    Jars = Jars / c + Jars % c;
  }
  return Total;
}

int main(void)
{
  int n, p, c;
  cout << "\nEnter n, p and c : ";
  cin >> n >> p >> c;
  cout << cookieCount(n, p, c);
}
