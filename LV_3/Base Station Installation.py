# https://programmers.co.kr/learn/courses/30/lessons/12979

# Input Example
n = 11              # the number of apartments
stations = [4,11]   # base station
w = 1               # totalW
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
for i in range(len(apart)):
    if apart[i] == 0:
        totalW+=1
    if totalW == maxW or (apart[i] == 1 and totalW > 0):
        answer += 1
        totalW = 0
        
#정확성/효율성: 53.7/0
