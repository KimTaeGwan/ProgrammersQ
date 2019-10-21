#https://programmers.co.kr/learn/courses/30/lessons/42861

#input
n = 4
costs = [[0,1,1],
         [2,3,1],
         [1,2,2]]
#return: 12

#solution
answer = 0
T = set()
costs = sorted(costs, key = lambda element: element[2])
for cost in costs:
    if len(T) == n:
        break
    if (cost[0] not in T) or (cost[1] not in T):
        T.add(cost[0])
        T.add(cost[1])
        answer += cost[2]
        
#정확성: 25
