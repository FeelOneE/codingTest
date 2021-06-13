# 등굣길
# https://programmers.co.kr/learn/courses/30/lessons/42898
# 계속되는 폭우로 일부 지역이 물에 잠겼습니다. 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다.
# 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.
# 아래 그림은 m = 4, n = 3 인 경우입니다.
# 가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래,
# 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.
# 격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다.
# 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를
# 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.


#DFS
#graph = { 'A' = ['B','C'], 'B' = ['D', 'E'] .. }
#visited = set()
#
#def dfs(visitied, graph, node):
#   if node not in visited:
#       print(node)
#       visited.add(node)
#	for neighbor in graph[node]:
#		dfs(visited, graph, neighbor)

def convertGraph(m,n,puddles):
    graph = dict()
    index = 1
    puddlesList = []
    for i in range(len(puddles)):
        puddlesList.append( (puddles[i][0]) + ((puddles[i][1]-1)*m) )
    print(puddlesList)
    for i in range(n):
        for j in range(m):
            if index not in puddlesList:
                listTmp = []
                if j != (m-1) and (index+1) not in puddlesList:
                    listTmp.append( index +1)
                if i != (n-1) and (index+m) not in puddlesList:
                    listTmp.append( index +m)
                graph[index] = list(listTmp)
            index = index + 1
    print(graph)
    return graph


def dfs(visited, graph, node):
   if node not in visited:
       print(node)
       #if node == 
       visited.add(node)
       for neighbor in graph[node]:
               dfs(visited, graph, neighbor)

def solution(m, n, puddles):
    answer = 0
    visited = set()
    graph = convertGraph(m,n,puddles)
    print(type(graph))
    print(type(graph[1]))
    dfs(visited, graph, 1)        

    return answer


if __name__ == "__main__":
    m = 4
    n = 3
    puddles = [[2, 2]]
    solution(m, n, puddles)
