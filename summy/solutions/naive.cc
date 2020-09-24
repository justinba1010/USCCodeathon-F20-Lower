#include <stdlib.h>
#include <iostream>
#include <algorithm>

using std::cin;
using std::cout;
int MAX = -10000;
int MIN = 10000;

int get_min(int *arr, int len) {
  int min = MIN;
  int index = -1;
  for (int i = 0; i < len; ++i) {
    if (arr[i] < min) {
      min = arr[i];
      index = i;
    }
  }
  arr[index] = MIN;
  return min;
}

int get_max(int *arr, int len) {
  int max = MAX;
  int index = -1;
  for (int i = 0; i < len; ++i) {
    if (arr[i] > max) {
      max = arr[i];
      index = i;
    }
  }
  arr[index] = MAX;
  return max;
}

int main(int argc, char *argv[]) {
  int n, k;
  cin >> n;
  cin >> k;
  int arr[n];
  int arr2[n];
  for (int i = 0; i < n; ++i) {
    cin >> arr[i];
    arr2[i] = arr[i];
  }
  int min = 0;
  int max = 0;
  for (int i = 0; i < k; ++i) {
    min += get_min(arr, n);
    max += get_max(arr2, n);
  }
  cout << min << "\n" << max << "\n";
  return 0;
}

