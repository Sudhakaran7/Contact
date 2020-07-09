a=int(input())
arr=list(map(str,input().split()))
stack=[]
res=[]
for i in range(0,len(arr)):
  stack.append(arr[i])
for i in range(0, len(stack)):    
    for j in range(i+1, len(arr)):    
        if(stack[i] ==stack[j]):    
            res.append(stack[i])
for i in range(len(res)):
  print(res.pop())
