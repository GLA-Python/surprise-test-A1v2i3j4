print("enter list of integers")
s=eval(input())
def expanding(k ):
    v=[]
    for i in range(0,len(k)-1):
        diff1=abs(k[i+1]-k[i])
        v.append(diff1)
    
    for j in range(0,len(v)-1):
        diff2=v[j+1]-v[j]
        if diff2>0:
            q=1
        else:
            q=0
    if q==1:  
        print("true")
    else:
        print("false")
expanding(s)

