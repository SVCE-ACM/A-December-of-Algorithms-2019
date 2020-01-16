/*
Author - Nilesh D
December 6 - Fibonacci Prime number generation
*/

#include <iostream>

using namespace std;

bool isPrime(int num)
{
  if (num == 0 || num == 1)
    return false;

  for (int i = 2; i * i < num; i++)
  {
    if (num % i == 0)
    {
      return false;
    }
  }
  return true;
}

int main(void)
{
  int n;
  cout << "\nEnter the value for (n): ";
  cin >> n;
  int t1 = 0;
  int t2 = 1;
  int next_term;
  cout << "Generated Fibonacci Prime Number Generation upto (" << n << "): \n";
  for (int i = 0; i < n;)
  {
    if (isPrime(t1))
    {
      i++;
      cout << t1;
      if (i != n)
        cout << ", ";
    }
    next_term = t1 + t2;
    t1 = t2;
    t2 = next_term;
  }
}
