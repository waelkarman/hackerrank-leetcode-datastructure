def biggerIsGreater(w):
    # Write your code here
    a=len(w)-1
    b=len(w)-2
    h=0
    k=0
    index_sum=0
    while(a>=k+1):
        while(b>=k):
            if(w[b]<w[a]):
                if( a>h or b>k ):
                    h=a
                    k=b
                if( (a+b) >= index_sum ):
                    index_sum=a+b
                    h=a
                    k=b
            b-=1
        
        a-=1
        b=a-1
    
    if(h==0 and k==0):
        return "no answer"
    #swap
    tmp=w[h]
    l=list(w)
    l[h]=w[k]
    l[k]=tmp
    w=''.join(l)
    #sort 
    l1=list(w[k+1:len(w)])
    l1.sort()

    return w[0:k+1]+''.join(l1)
