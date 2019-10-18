#https://programmers.co.kr/learn/courses/30/lessons/42884

#input
routes = [[-20,15],
          [-5,-3],
          [-14,-5],
          [-18,-13]
          ]
#return 2

#solution

answer = 1
routes = sorted(routes,reverse=True)
cam = routes[0][0]

for start,end in routes:
    if start > cam or end < cam:
        cam = start
        answer += 1
    
# 오답없음
