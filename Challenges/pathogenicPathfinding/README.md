# Pathogenic Pathfinding


This was just a standard pathfinding problem with a slight twist. Firstly, in solving a 
pathfinding problem like this where the goal is to find the shortest distance between 2 nodes 
of a cyclical, bidirectional graph with only positive connections you can use dijkstras algorthimn.

Here is the pseudocode for Dijkstra's Algoritihmn pulled from wikipedia:

1. Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.

2. Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. The tentative distance of a node v is the length of the shortest path discovered so far between the node v and the starting node. Since initially no path is known to any other vertex than the source itself (which is a path of length zero), all other tentative distances are initially set to infinity. Set the initial node as current.

3. For the current node, consider all of its unvisited neighbors and calculate their tentative distances through the current node. Compare the newly calculated tentative distance to the current assigned value and assign the smaller one. For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbor B has length 2, then the distance to B through A will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, the current value will be kept.

4. When we are done considering all of the unvisited neighbors of the current node, mark the current node as visited and remove it from the unvisited set. A visited node will never be checked again.

5. If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished.

6. Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new current node, and go back to step 3.


What this algorithm does is finds the minimum distance to all nodes from 1 singular node. Thus if you 
were to use this on say Node A, you would have the minimum distance from A to every other node in the 
graph. Just doing this would be enough to get the first 15 test cases however you would time out
on the rest of them.

The reason for this time out is due to the nature of the question that was asked. If you go back
and read the problem statement you will see that you are asked to find MULTIPLE distances between
nodes, not just 1. Imagine I asked you to find the distance between A and B 5000 times. Unless you
made your code remember what you've already calculated, you would spend forever calulating the
same thing over and over again.

Thus the twist for this problem involved "CACHING", which means storing your results after each calculation in a way that you can remember them. The way I implemented this was a shortest
paths matrix that was originally given values of INFTY (99999999). If the matrix contained any other
value besides INFTY, it would simply print the value out intead of using dijkstras. This reduced
the complexity of the problem and allowed my solution to run in time.