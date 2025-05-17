#union of two sorted arrays

ls1=[1,2,2,3,9]
ls2=[1,2,3,4,6]

i,j=0,0
ls3=[]
while i<len(ls1) and j<len(ls2):
    if(ls1[i]<=ls2[j]):
        if len(ls3)==0 or ls1[i]!=ls3[-1]:
            ls3.append(ls1[i])
           
        i+=1
    else:
        if len(ls3)==0 or(ls2[j]!=ls3[-1]):
           ls3.append(ls2[j])
        j+=1
while i<len(ls1):
    if len(ls3)==0 or(ls1
                      [i]!=ls3[-1]):
        ls3.append(ls1[i])
    i+=1
               

while j<len(ls2):
    if len(ls3)==0 or(ls2[j]!=ls3[-1]):
        ls3.append(ls2[j])
    j+=1
    
print(ls3)
               
