# https://programmers.co.kr/learn/courses/30/lessons/12979

# Input Example
n = 10              # the number of apartments
stations = [5]   # base station
w = 4               # totalW
# answer = 3


answer = 0
apart = [0 for i in range(n)]
for station in stations:
    station -= 1
    for i in range(station-w,station+w+1):
        if i < 0: continue
        elif i > n-1: break
        else: apart[i]=1

maxW = (2*w) + 1
totalW = 0
for i in range(n):
    if apart[i] == 0:
        totalW+=1
    if totalW == maxW or (apart[i] == 1 and totalW > 0):
        answer += 1
        totalW = 0

if totalW > 0:
    answer+=1
        
#정확성/효율성: 70.5/0
