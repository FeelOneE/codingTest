#정수 삼각형 문제
#https://programmers.co.kr/learn/courses/30/lessons/43105
#위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.
#삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.
#
#Idea : 양 끝쪽의 삼각형의 면은 무조건 다음 줄에서, 0이면 0, 끝이면 +1
#       둘 다 아니면 비교해서 max 값

def solution(triangle):
    
    for triangleIndex in range(1,len(triangle)):
        for itemIndex in range(0,len(triangle[triangleIndex])):
            if itemIndex == triangleIndex:
                triangle[triangleIndex][itemIndex] += triangle[triangleIndex-1][itemIndex-1]
            elif itemIndex == 0:
                triangle[triangleIndex][itemIndex] += triangle[triangleIndex-1][itemIndex]
            else:
                triangle[triangleIndex][itemIndex] += max(triangle[triangleIndex-1][itemIndex],triangle[triangleIndex-1][itemIndex-1])
    return max(triangle[-1])