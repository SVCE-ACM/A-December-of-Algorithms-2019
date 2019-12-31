#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

/*
O(1) Solution

Let number of bulbs be n.
Iteration 1 : n bulbs are on 
Iteration 2 : Turn off every second bulb (2,4,6,..)
Iteration 3 : Toogle every third bulb (3,6,9,...)

Iteration i: Toggle every ith bulb (i,2i,3i,...)
Iteration n: Toggle only last bulb (n).

Let us take a case n=6.
Bulb is toggled in iteration 2 and 3.
Bulb 6 is toggled also in the last round. This is the last time it will be toggled.

Factors of 6:2,3,6,1 (Ignore 1 since all bulbs are on in first iteration)

Thus, a bulb 'i' is toggled k times.
k is the number of factors of i. (Except 1)
Total number of factors of i = k + 1

Now, we have to determine if k is odd or even.
All bulbs are on at the beginning,
if k is odd, bulb will be off at the end.
if k is even, bulb will be on at the end.

We know that only all perfect squares (4,9,16) have squares have an odd number of factors.
All other numbers have an even number of factors.

Thus, if i is a perfect square, k + 1 is odd and hence k is even.
If i is not a perfect square, k + 1 is even and hence k is odd.

To find out how many bulbs are on at the end,
We have to calculate the number of perfect squares not greater than number of bulbs.

This is basically the integer part of sqrt(n).
*/

int numOfBulbs_O_1(int n)
{
  return sqrt(n);
}

int numOfBulbs_O_n(int n)
{
  int Count = 0;
  for (int i = 1; i < n + 1; i++)
  {
    if (i * i < n + 1)
    {
      Count++;
    }
  }
  return Count;
}

int main(void)
{
  int n;
  cout << "\nEnter number of bulbs : ";
  cin >> n;
  cout << "\nNumber of bulbs in 'on' state (O(1) solution) : " << numOfBulbs_O_1(n);
  cout << "\nNumber of bulbs in 'on' state (O(n) solution) : " << numOfBulbs_O_n(n);
  return 0;
}
