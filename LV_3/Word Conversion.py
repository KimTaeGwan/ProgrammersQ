#https://programmers.co.kr/learn/courses/30/lessons/43163

#input
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
#return: 4

#solution
import queue
Q = queue.Queue()
Q.put(begin)
h = {}
h[begin] = 0

while Q.qsize() > 0:
    begin = Q.get()
    for word in words:
        wCount = 0
        for i in range(len(target)):
            if begin[i] == word[i]:
                wCount += 1
            if (wCount == len(target)-1) and (word not in h):
                h[word] = h[begin]+1
                Q.put(word)
         
    
if target not in h:
    answer = 0
else:
    answer = h[target]
        
#오답 없
        
