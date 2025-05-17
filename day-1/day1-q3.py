
#largest len of continious 1`s
ar=[0,1,1,0,1,1,1,0,0,1]
i=0
j=0
max_count=0
count=0
while i<len(ar) and j<len(ar):
    if(ar[i]==1):
        if(ar[j]==1):
            count+=1
            j+=1
            
        else:
            if count>max_count:
                max_count=count
            count=0
            i=j
    else:
        i+=1
        j+=1
print(max_count
      )
            
            
        
    
