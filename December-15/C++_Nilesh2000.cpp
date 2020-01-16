/*
Author - Nilesh D 
December 15 - Intruder Alert
*/

#include <iostream>
#include <string>

using namespace std;

void totalQuantity(int n, string Str = "", int a = 0, int b = 0)
{
  if (a == b && a == n)
  {
    cout << Str << " ";
  }
  if (a <= n)
  {
    totalQuantity(n, Str + "A", a + 1, b);
    if (b < a)
    {
      totalQuantity(n, Str + "B", a, b + 1);
    }
  }
}

int main(void)
{
  int quantityOfA;
  cout << "\nEnter the quantity of A : ";
  cin >> quantityOfA;
  totalQuantity(quantityOfA);
}