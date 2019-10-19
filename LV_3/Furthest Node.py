#https://programmers.co.kr/learn/courses/30/lessons/49189

#input
n = 6
vertex = [[3, 6],
          [4, 3],
          [3, 2],
          [1, 3],
          [1, 2],
          [2, 4],
          [5, 2]]
#return 3

#solution

import queue

Q = queue.Queue()
Q.put(1)
h = {}
h[1] = 0

while Q.qsize() > 0:
    u = Q.get()
    for v in vertex:
        if (u == v[0]) and (v[1] not in h):
            Q.put(v[1])
            h[v[1]] = h[u]+1
        elif u == v[1] and (v[0] not in h):
            Q.put(v[0])
            h[v[0]] = h[u]+1
            
h = list(h.values())
answer = h.count(h[-1])

#정확성: 66.7, 테스트 7,8,9 시간 초
