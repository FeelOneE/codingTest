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


# DFS
# graph = { 'A' = ['B','C'], 'B' = ['D', 'E'] .. }
#visited = set()
#
# def dfs(visitied, graph, node):
#   if node not in visited:
#       print(node)
#       visited.add(node)
#	for neighbor in graph[node]:
#		dfs(visited, graph, neighbor)

#global 변수


#웅덩이 판별 함수
def isPuddle(m,n,puddles):
    check = False
    if len(puddles) > 0:
        for pud in puddles:
            if pud[0] == n and pud[1] == m:
                return True
    return check

#인접 그래프로 변환
def convertGraph(m, n, puddles):
    graph = [ [0 for _ in range(m*n+1)] for _ in range(m*n+1)  ]
    index = 1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            #print("i,j :",i,",",j)
            if isPuddle(i,j,puddles) == False:
                if j != m and isPuddle(i,j+1,puddles) == False:
                    graph[index][index+1] = 1
                    #print(index,", ",index+1," is connect")
                if i != n and isPuddle(i+1,j,puddles) == False:
                    graph[index][index+m] = 1
                    #print(index,", ",index+m," is connect")
            index = index + 1
    #for g in graph:
        #print(g)
    return graph

visit = []
stack = []
count =0

def dfs(graph, curr, end):
    global visit
    global stack
    global count
    #print("append stack :", curr)
    stack.append(curr)
    visit[curr] = True
    if curr == end:
        #print(stack)
        count = count + 1
        visit[curr] = False
        stack.pop()
        return    
    for i in range(len(graph)):
        if graph[curr][i] == 1:
            visit[curr] = False
            dfs(graph, i, end)
    stack.pop()
    
def solution(m, n, puddles):
    answer = 0
    global visit
    global count
    visit = [0 for _ in range(m*n+1)]
    graph = convertGraph(m, n, puddles)
    dfs(graph, 1, m*n)
    answer = count
    return answer


if __name__ == "__main__":
    m = 3
    n = 4
    puddles = [[2, 2]]
    print(solution(m, n, puddles))
