import heapq
arr=[2,3,1,4,15,7,6,18,9,15,13]
l=[]
heapq.heapify(l)
i=0
n=len(arr)
while i<n:
    if len(l)<2:
        heapq.heappush(l,arr[i])
    else:
        if l[0]<arr[i]:
            heapq.heappop(l)
            heapq.heappush(l,arr[i])
    i+=1
print(heapq.heappop(l))
    
