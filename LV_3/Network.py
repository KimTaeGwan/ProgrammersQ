#https://programmers.co.kr/learn/courses/30/lessons/43162

#input
n = 3
computers = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
#return: 1


#solution

def DPS(x):
    visited[x] = True
    for i in range(n):
        if computers[x][i] == 1 and visited[i] == False:
            DPS(i)
            
visited = [False for _ in range(3)]
answer = 0
for i in range(n):
    if visited[i] == False:
        DPS(i)
        answer += 1

# 오답 없음 

        

