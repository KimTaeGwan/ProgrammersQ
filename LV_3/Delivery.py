#https://programmers.co.kr/learn/courses/30/lessons/12978

#input ex
n = 5
road = [[1,2,1], # N1: 1, N2: 2, N1<->N2: 1
        [2,3,3],
        [5,2,2],
        [1,4,2],
        [5,3,1],
        [5,4,2]]

k = 3
#result = 4


#solution
answer = 0
L = [[] for i in range(n+1)]
for road in road:
    L[road[0]].append([road[1],road[2]])
    L[road[1]].append([road[0],road[2]])

D = [10000 for i in range(n+1)]
D[1] = 0

V = [i for i in range(n+1)]
while len(V) != 1:
    minNum = 10000
    for i in V:
        if D[i] < minNum:
            minNum = D[i]
            u = i
    V.remove(u)
    
    for l in L[u]:
        if D[l[0]] > l[1] + D[u]:
            D[l[0]] = l[1] + D[u]

for i in D:
    if i <= k:
        answer+=1
            
#정확성 90.6/100, test30,31,32 런타임 에러            

