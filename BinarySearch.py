def binary_search(a,x,start,end):
    if x in a:
        
        b=(start+end)//2
        if(a[start]==x):
            return start
        elif(a[end]==x):
            return end
        elif(a[b]==x):
            return b
        elif(a[start]!=x and a[end]!=x):
            if(a[b]>x):
                return binary_search(a,x,start,b)
            else:
                return binary_search(a,x,b,end)
    
    else:
        return "Not Present in the list"
a=[1,2,3,4,5,5,9,4,24,435,2342,2524,500000]
n=len(a)

print(binary_search(a,24,0,n-1))
print(binary_search(a,2676,0,n-1))
