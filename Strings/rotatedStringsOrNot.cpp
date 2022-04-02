#include <bits/stdc++.h>

using namespace std;

using namespace std;

bool checkRotation(string a, string b) {

  if (a.size() != b.size()) {
    return false;
  }

  //now we have two strings of equal length;

  //get first char of string a;
  int index_a = 0;

  //find this char in string b, and mark index as j;
  int index_b = INT_MIN;
  for (int i = 0; i < b.size(); i++) {
    if (b[i] == a[0]) {
      index_b = i;
      break;
    }
  }

  //what if not found?
  if (index_b == INT_MIN) {
    return false;
  }

  //we are here, means we have starting char in both strings
  //for the second string, we will wrap around;
  int count = a.size(); //max till size of string it will iterate
  int step = 0;
  while (step < count) {
    if (a[index_a] != b[index_b]) {
      return false;
    }
    index_a++;
    index_b = (index_b + 1) % b.size();

    step++;
  }
  return true;
}
int main() {
  string a, b;
  cin >> a;
  cin >> b;
  cout << "Inputted Strings are  : " << a << " " << b << endl;

  bool ans = checkRotation(a, b);
  if (ans) {
    cout << "Strings are rotated wrt each other";
  } else {
    cout << "Strings are not rotated wrt each other";
  }
  return 0;

}