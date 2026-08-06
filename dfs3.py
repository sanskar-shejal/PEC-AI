graph={
    'Root':['A','B'],
    'A':['C','D'], 
    'B':['E','F'],
    'C':['G','H'],
    'D':['I','J'],
    'E':[],
    'F':[],
    'G':['K','L'],
    'H':[],
    'I':['M','N'],
    'J':[],
    'K':[],
    'L':[],
    'M':[],
    'N':[]
    }
visited=set()

def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

print("Following is the Depth-First Search")
dfs(visited,graph,'Root')