
def solution(N,number):
    if N == number : return 1
    S = [{int(str(N)*(x+1))} for x in range(8)]
    answer = -1
    #print(S)
    for i in range(1, len(S)):
        for j in range(i):
            for k in S[j]:
                for h in S[i-j-1]:
                    S[i].add(k + h)
                    S[i].add(k - h)
                    S[i].add(k * h)
                    if h != 0:
                        S[i].add(k//h)

        if number in S[i]:
            answer = i + 1
            break

    return answer

if __name__ == "__main__" :
    N = 5
    number = 12
    print(solution(N, number))
