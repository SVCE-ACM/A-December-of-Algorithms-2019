/*
Author - Nilesh D
December 27 - Spiralling
*/

#include <iostream>

using namespace std;

void printSpiral(int Arr[10][10], int m, int n)
{
  int rowStart = 0, colStart = 0, matIter;
  while (rowStart < m && colStart < n)
  {
    // Print first row
    for (matIter = colStart; matIter < n; matIter++)
    {
      cout << Arr[rowStart][matIter] << " ";
    }
    rowStart++;

    // Print last column
    for (matIter = rowStart; matIter < m; matIter++)
    {
      cout << Arr[matIter][n - 1] << " ";
    }
    n--;

    // Print last row
    if (rowStart < m)
    {
      for (matIter = n - 1; matIter >= colStart; matIter--)
      {
        cout << Arr[m - 1][matIter] << " ";
      }
      m--;
    }

    // Print first column
    if (colStart < n)
    {
      for (matIter = m - 1; matIter >= rowStart; matIter--)
      {
        cout << Arr[matIter][colStart] << " ";
      }
      colStart++;
    }
  }
}

int main(void)
{
  int Rows, Cols;
  cout << "\nEnter number of rows and columns : ";
  cin >> Rows >> Cols;
  int Arr[10][10];
  for (int i = 0; i < Rows; i++)
  {
    for (int j = 0; j < Cols; j++)
    {
      cin >> Arr[i][j];
    }
  }
  printSpiral(Arr, Rows, Cols);
}
