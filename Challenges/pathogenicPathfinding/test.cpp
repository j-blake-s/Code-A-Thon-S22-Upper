#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <map>
using namespace std;


const int INFTY = 999999999; //? 9.99r * 10^8

string my_argmin(vector<string> &keys) {

  string best = keys[0];

  swap(keys[0],keys.back());
  
  keys.pop_back();
  return best;

}



int main() {
  vector<string> vec = {"hello","there","oswald"};

  cout << my_argmin(vec) << endl;
  cout << vec.front() << endl;
  cout << vec.back() << endl;
}