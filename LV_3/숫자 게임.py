answer = 0
A = [2,2,2,2] # fixing
B = [1,1,1,1] #  
#result = 3

count = 0
A.sort(reverse=True)
for i in range(len(A)):
    if A[i] < max(B):
        B.remove(max(B))
        count+=1
    else:
        B.remove(min(B))
        
