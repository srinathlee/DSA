#pushing 0`s to end of array
arr=[1,0,4,0,6,0,9]
position=0
for i in arr:
    if i!=0:
        arr[position]=i
        position+=1
for j in range(position,len(arr)):
    arr[j]=0
print(arr)
