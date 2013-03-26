import sys
import math
import itertools

# function Dijkstra(Graph, source):
#       for each vertex v in Graph:                                // Initializations
#           dist[v] := infinity ;                                  // Unknown distance function from 
#                                                                  // source to v
#           previous[v] := undefined ;                             // Previous node in optimal path
#       end for                                                    // from source
      
#       dist[source] := 0 ;                                        // Distance from source to source
#       Q := the set of all nodes in Graph ;                       // All nodes in the graph are
#                                                                  // unoptimized - thus are in Q
#       while Q is not empty:                                      // The main loop
#           u := vertex in Q with smallest distance in dist[] ;    // Source node in first case
#           remove u from Q ;
#           if dist[u] = infinity:
#               break ;                                            // all remaining vertices are
#           end if                                                 // inaccessible from source
          
#           for each neighbor v of u:                              // where v has not yet been 
#                                                                  // removed from Q.
#               alt := dist[u] + dist_between(u, v) ;
#               if alt < dist[v]:                                  // Relax (u,v,a)
#                   dist[v] := alt ;
#                   previous[v] := u ;
#                   decrease-key v in Q;                           // Reorder v in the Queue
#               end if
#           end for
#       end while
#   return dist;


def djikstra(graph, start, end):
    oo = math.infinity

    dist = [[oo for x in y] for y in graph]
    previous = [[0 for x in y] for y in graph]

    dist[start[0]][start[1]] = 0
    Q = itertools.chain(*graph)

    while Q:
        u = min(dist, lambda x, y: x < y && x in Q))


def main():
    while(True):
        size = int(sys.stdin.readline())

        if size == 0:
            break

        graph = []

        for x in xrange(size):
            graph.append([int(x) for x in sys.stdin.readline().split()])

        graph = zip(*graph)

        start = (0, 0)
        end = (size - 1, size - 1)

        djikstra(graph, start, end)

if __name__ == '__main__':
    main()
