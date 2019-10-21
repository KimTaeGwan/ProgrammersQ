#https://programmers.co.kr/learn/courses/30/lessons/42861

#input
n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]  
#return:

#solution
answer = 0
edge = 0
G = [i for i in range(n)]
costs = sorted(costs, key = lambda element: element[2])
print(costs)
for cost in costs:
    if edge == n-1:
        break
    if G[cost[0]] != G[cost[1]]:
        if cost[0] > cost[1]:
            G[cost[0]] = G[cost[1]]
        else:
            G[cost[1]] = G[cost[0]]
        print(G)
        answer += cost[2]
        edge+=1
        
#정확성: 50
    
