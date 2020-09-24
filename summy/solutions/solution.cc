#include <stdlib.h>
#include <iostream>
#include <algorithm>

using std::cin;
using std::cout;
using std::sort;

int main(int argc, char *argv[]) {
  int n, k;
  cin >> n;
  cin >> k;
  int arr[n];
  for (int i = 0; i < n; ++i) {
    cin >> arr[i];
  }
  int min = 0;
  int max = 0;
  sort(arr, arr + n);
  for (int i = 0; i < k; ++i) {
    min += arr[i];
    max += arr[n-i-1];
  }
  cout << min << "\n" << max << "\n";
  return 0;
}

