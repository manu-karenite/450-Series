#include <bits/stdc++.h>

using namespace std;

int main() {
  string nam;
  getline(cin, nam);

  unordered_map < char, int > umap;
  for (int i = 0; i < nam.size(); i++) {
    if (nam[i] == ' ') continue;
    umap[nam[i]]++;
  }
  for (int i = 0; i < nam.size(); i++) {
    char key = nam[i];
    if (umap[key] > 1) {

      cout << key << " " << umap[key] << endl;
      umap.erase(key);
    }
  }
  return 0;
}