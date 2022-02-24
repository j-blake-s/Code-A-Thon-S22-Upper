#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <queue>
#include <map>
using namespace std;

/* ----------------------------------------------- */
const size_t qSize = 2;
const size_t cSize = 3;
const size_t argSize = 3;
const int INFTY = 999999999; //? 9.99r * 10^8
int min_dist = INFTY;
/* ----------------------------------------------- */


/* ---------------------------------------------------------------------------------------------- */
string input();
int toInt(string);
string* split(string,int);
void sol(map<string,map<string,int>>,int,string**,int);
void print_map(map<string,map<string,int>>);
void dijkstra(map<string,map<string,int>>,int, map<string,map<string,int>>&, vector<string>, string);
string my_argmin(vector<string>&, map<string,int>);
bool contains(vector<string>,string);
void depth(map<string,map<string,int>>,string,string,int,vector<string>&);
/* ---------------------------------------------------------------------------------------------- */

int main() {  

  //? Get the first line arguements
  string* args = split(input(),argSize); 
  int numNodes = toInt(args[0]);
  int numConnections = toInt(args[1]);
  int numQs = toInt(args[2]);



  //? Read the connections
  std::map<string,std::map<string,int>> graph;
  for (int i = 0; i < numConnections; i++) {
    string* connection = split(input(),cSize);
    string nodeA = connection[0];
    string nodeB = connection[1];
    int cost = toInt(connection[2]);
    graph[nodeA][nodeB] = cost;
    graph[nodeB][nodeA] = cost;
    delete [] connection;
  }


  //? Read the Queries
  string** Qs = new string*[numQs];
  for (int i = 0; i < numQs; i++) {
    Qs[i] = split(input(),qSize);
  }

  sol(graph,numNodes,Qs,numQs);

  //? Freeing memory
  for (int i = 0; i < numQs; i++) {
      delete [] Qs[i];
  }

  delete [] Qs;
  delete [] args;
}


int min(int a, int b) {
  if (a < b) return a;
  return b;
}
void depth(map<string,map<string,int>> graph,string current,string end,int dist, vector<string>& visited) {

  if (current == end) {
    min_dist = min(min_dist,dist);
    return;
  }

  for (const auto& n : graph[current]) {
    if (!contains(visited,n.first)) {
      visited.push_back(n.first);
      depth(graph,n.first,end,dist+graph[current][n.first],visited);
      visited.pop_back();
    }
  }
}
  

void sol(map<string,map<string,int>> graph,int numNodes, string** Qs, int numQs) {


  //? Create vector of nodes
  vector<string> nodes;

  //? Solve
  for (int nQ = 0; nQ < numQs; nQ++) {
    min_dist = INFTY;
    string* Q = Qs[nQ];
    string from = Q[0];
    string to = Q[1];
    depth(graph,from,to,0,nodes);
    cout << min_dist << endl;
  }
}


//? Like python or java split
//? Make sure to delete nodes later
string* split(string s,int size) {
  string* nodes = new string[size];
  std::stringstream ss(s);

  string temp;
  int count = 0;
  while(getline(ss,temp,' ')) nodes[count++] = temp;
    
  return nodes;
}

int toInt(string anInt) {return std::stoi(anInt);}
string input() {string tempWord; getline(cin,tempWord);return tempWord;}
bool contains(vector<string> vec, string target) {for (auto e : vec) if (e == target) return 1;return false;}

