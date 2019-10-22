#https://programmers.co.kr/learn/courses/30/lessons/43237

#input
budgets = [120,110,140,150,90]
M = 1000
#return 127

#solution

L = 0
H = 0
totalBuget = 0 
for buget in budgets:
    H = max(H,buget)
    totalBuget += buget

if totalBuget <= M:
    print("end")

while L <= H:
    totalBuget = 0
    Mid = (L+H) // 2
    for buget in budgets:
        if buget > Mid:
            buget = Mid
        totalBuget += buget
        
    if totalBuget <= M:
        answer = Mid
        L = Mid + 1
    else:
        H = Mid - 1
        
        
# 오답 없음

