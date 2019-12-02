/*
Started On : December 1, 2019
Author : Nilesh D
Objective : Output the nth sevenish number
*/

# include <iostream>
# include <vector>
# include <cmath>

using namespace std;

int get_nth_sevenish(int n)
{
  int power = 0;
  vector<int> sevenish_nums;
  while(sevenish_nums.size() < n)
  {
    int num = pow(7, power);
    vector<int> new_sevenish_nums{num};
    for(auto&& iter : sevenish_nums)
    {
      if(sevenish_nums.size() + new_sevenish_nums.size() == n)
        return new_sevenish_nums.back();
      new_sevenish_nums.push_back(num + iter);
    }
    sevenish_nums.insert(sevenish_nums.end(), new_sevenish_nums.begin(), new_sevenish_nums.end());
    power++;
  }
  return sevenish_nums.back();
}

int main(void)
{
  int n;
  cout << "\nEnter value of n : ";
  cin >> n;
  cout << get_nth_sevenish(n);
  return 0;
}
