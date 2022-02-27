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


void dijkstra(map<string,map<string,int>> graph, int numNodes, 
              map<string,map<string,int>>& sp,
              vector<string> nodes,
              string start) {


  //? While there are unvisited nodes
  while (nodes.size() > 0) {


    //? Find unvisited node with minumum distance to start node.
    string minNode = my_argmin(nodes,sp[start]);

    //? Look at every edge originating from minNode
    for (const auto& edge : graph[minNode]) {
      
      //? If the edge has been visited, ignore it.
      if (contains(nodes,edge.first)) {
      // if (contains(pQ,edge.first)) {
        int alt = sp[start][minNode] + graph[minNode][edge.first];
        if (alt < sp[start][edge.first]) {
          sp[start][edge.first] = alt;
        }
      }
    }
  }
}

void sol(map<string,map<string,int>> graph,int numNodes, string** Qs, int numQs) {

  //? Create vector of nodes
  vector<string> nodes;

  //? Create shortest path map
  map<string,map<string,int>> sp;
  int val = INFTY;
  for (const auto& n : graph) {
    nodes.push_back(n.first);
    for (const auto& m : graph) {
      if (n.first == m.first) val = 0;
      else val = INFTY;
      sp[n.first][m.first] = val;
    }
  }

  for (int i = 0; i < numNodes; i++) {
    dijkstra(graph,numNodes,sp,nodes,nodes[i]);
  }

  for (int nQ = 0; nQ < numQs; nQ++) {
    string* Q = Qs[nQ];
    string from = Q[0];
    string to = Q[1];
    cout << sp[from][to] << endl;
  }
  // //? Solve
  // for (int nQ = 0; nQ < numQs; nQ++) {
  //   string* Q = Qs[nQ];
  //   string from = Q[0];
  //   string to = Q[1];

  //   //? Only compute distance if not already found
  //   if (sp[from][to] == INFTY) {
  //     dijkstra(graph,numNodes,sp,nodes,from,to);
  //     //sp[to][from] = sp[from][to];
  //   }
  //   cout << sp[from][to] << endl;
  // }
}

//? Using a vector of valid keys, find the the key with the lowest associated cost in keyMap
string my_argmin(vector<string> &keys, map<string,int> keyMap) {

  //? Find min key
  int min = INFTY;
  int argmin = -1;
  for (size_t i = 0; i < keys.size(); i++) {
    int val = keyMap[keys[i]];
    if (val < min) {
      min = val;
      argmin = (int)i;
    }
  }

  //? Pop the min key from the vector
  string best = keys[argmin];
  swap(keys[argmin],keys.back());
  keys.pop_back();
  return best;
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

