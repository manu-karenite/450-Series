#include <bits/stdc++.h>

using namespace std;

using namespace std;

bool checkRotation(string a, string b, string c) {
  unordered_map < char, int > umap;

  for (int i = 0; i < c.size(); i++) {
    umap[c[i]]++;
  }
  for (int i = 0; i < a.size(); i++) {
    if (umap[a[i]] <= 0) {
      return false;
    }
    //otherwise exists
    umap[a[i]]--;
  }
  for (int i = 0; i < b.size(); i++) {
    if (umap[b[i]] <= 0) {
      return false;
    }
    //otherwise exists
    umap[b[i]]--;
  }
  return true;

}
int main() {
  string a, b, c;
  cin >> a;
  cin >> b;
  cin >> c;
  cout << "Inputted Strings are  : " << a << " " << b << endl;

  bool ans = checkRotation(a, b, c);
  if (ans) {
    cout << c << " are shuffled with " << a << " " << b << endl;;
  } else {
    cout << c << " are not shuffled with " << a << " " << b << endl;
  }
  return 0;

}