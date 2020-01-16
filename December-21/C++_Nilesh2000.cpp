/*
Author - Nilesh D
December 21 - Marching Partners
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
  int n, Num;
  vector<int> V;
  cout << "\nEnter number of students : ";
  cin >> n;
  cout << "Enter heights of the " << n << " students : ";
  for (int i = 0; i < n; i++)
  {
    cin >> Num;
    V.push_back(Num);
  }
  sort(V.begin(), V.end());
  int maxHeightDifference;
  cout << "Enter the maximum height difference : ";
  cin >> maxHeightDifference;
  int Iter = 0, Count = 0;
  while (Iter < V.size() - 1)
  {
    if (abs(V[Iter] - V[Iter + 1]) <= maxHeightDifference)
    {
      Count++;
      Iter++;
    }
    Iter++;
  }
  cout << "Maximum number of possible pairs is : " << Count;
}
