#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int calculateHIndex(vector<int> citations, int Size)
{
  sort(citations.begin(), citations.end());
  int hIndex = 0;
  for (int i = 0; i < Size; i++)
  {
    if (citations[i] >= Size - i)
    {
      return Size - i;
    }
  }
  return 0;
}

int main(void)
{
  int n, Cite;
  cout << "\nEnter N : ";
  cin >> n;
  vector<int> V;
  cout << "Enter the citations of each paper : ";
  for (int i = 0; i < n; i++)
  {
    cin >> Cite;
    V.push_back(Cite);
  }
  cout << "The h-index is : " << calculateHIndex(V, n);
}
