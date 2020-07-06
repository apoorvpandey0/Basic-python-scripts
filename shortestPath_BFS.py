#Find the shortest path between two
#nodes in an unweighted graph using Breadth first Search algorithm
g = {  0:[1,9],
       1:[0,8],
       2:[3,8],
       3:[2,4,5],
       4:[3],
       5:[3,6],
       6:[5,7],
       7:[8,11,10,6],
       8:[7,1,9,2],
       9:[0,8,10],
       10:[7,11,9],
       11:[7,10]}

n= len(g)
def solve(s):
    q = [s]
    visited = [False for i in range(n)]
    visited[s] = True
    prev = [None for i in range(n)]

    while len(q):
        # print(prev)
        # print(q)
        node = q[0]
        neighbours = g[node]

        #Visit each neighbour mark them visited and set their previous node with prev[next] = node
        for next in neighbours:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                prev[next] = node

        #Start from the beginning of the queue
        q = q[1:]
    return prev

def reconstructPath(s,e,prev):
    #Reconstruct the path going backwards from e
    path = []
    at = e
    while at!=None :
        path.append(at)
        print(path)
        at = prev[at]
    path= path[::-1]

    if path[0] == s:
        return path
    return []

#s = startNode, e=endNode, and e>=0,s<n
def bfs(s,e):

    # Do a BFS search starting at node s
    prev  = solve(s)

    # Return reconstructed path from s -> e
    return reconstructPath(s,e,prev)
print(bfs(1,11))
