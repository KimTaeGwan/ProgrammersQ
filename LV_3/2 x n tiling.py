#https://programmers.co.kr/learn/courses/30/lessons/12900

"""output ex
n = 4, result = 5
n = 5, result = 8
"""

#input 
n = 4

#solution
answer = 0

rowTile = n // 2

for i in range(1,rowTile+1):
    colTile = n - (i*2)
    if colTile == 0:
        answer += 1
    else:
        answer += colTile+i
answer += 1

#정확성: 0, 효율성: 0
