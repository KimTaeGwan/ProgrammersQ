#https://programmers.co.kr/learn/courses/30/lessons/49994

dirs = "LULLLLLLU"
#answer = 7

#solution
answer = -1
x = 5
y = 5
road = []
idx = 0
for dir in dirs:
    prev = [x,y]
    road.append([prev])
    if dir == "L": x-=1
    elif dir == "R": x+=1
    elif dir == "U": y += 1
    elif dir == "D": y -= 1

    if x == -1: x = 0
    elif x == 11: x = 10
    elif y == -1: y = 0
    elif y == 11: y = 10
    
    if [prev, [x,y]] in road or prev == [x,y]:
        road.pop()
    else:
        road[idx].append([x,y])
        idx+=1

answer = len(road)

# 정확도 35.0/100.0, test 8~20 실패
