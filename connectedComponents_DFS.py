a = {  0:[1,9],
       1:[0,8],
       2:[3],
       3:[2,4],
       4:[3],
       5:[3,6],
       6:[5],
       7:[11,10],
       8:[1,9],
       9:[0,8],
       10:[7,11],
       11:[7,10]}

n= len(a)
visited = [False for i in range(n)]
def findComponents():
    components = [None for i in range(n)]
    count = 0
    #Loop over each Node
    for node in range(n):
        print("Starting for :",node)
        #If its not visited the run DFS to capture its whole structure and increment count
        if visited[node] == False:
            count+=1
            dfs(node,count,components)
    return count,components
def dfs(at,count,components):
    if visited[at] == True : return
    visited[at] = True
    neighbours = a[at]
    components[at] = count
    print(" ",at)

    #Loop over all the neighbours of the node
    for next in neighbours:
        dfs(next,count,components)

print(findComponents())
