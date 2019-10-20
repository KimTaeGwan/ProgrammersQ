#https://programmers.co.kr/learn/courses/30/lessons/42861

#input
n = 4
costs = [[0,1,1],
         [0,2,2],
         [1,2,5],
         [1,3,1],
         [2,3,8]]
#return: 4

#solution

answer = 0

for i in range(n-1):
    Min = costs[0]
    for cost in costs:
        if Min[2] > cost[2]:
           Min = cost
    answer += Min[2]
    costs.remove(Min)

#정확성: 37.5 
