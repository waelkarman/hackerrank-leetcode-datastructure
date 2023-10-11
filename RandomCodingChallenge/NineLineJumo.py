
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    answer = "YES"
    k=abs(x1-x2)
    j=abs(x1+v1-x2-v2)               
    
    if(k != 0 and k==j):
        answer = "NO"
    if(j>k):
        answer = "NO"
    if(j<k):
        if(k%(v1-v2) != 0):
            q=k/(v1-v2)
            q=int(q)+1
            after1=abs(x1+q*v1-x2-q*v2)        
            after2=abs(x1+(q+1)*v1-x2-(q+1)*v2)
            if(after1 !=0 and  after2>after1):
                answer = "NO"
        
    return answer

