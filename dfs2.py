graph={
    '1':['2','3'],
    '2':['4','5'],
    '3':['6','7'],
    '4':['8'],
    '5':['9'],
    '6':['10'],
    '7':['11'],
    '8':['12'],
    '9':['13'],
    '10':['14'],
    '11':['15'],
    '12':[],
    '13':[],
    '14':[]
}
visited=set()

def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

print("Following is the Depth-First Search")
dfs(visited,graph,'1')