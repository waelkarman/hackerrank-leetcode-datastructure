def plusMinus(arr):
    # Write your code here
    n1=0.000001
    n2=0.000001
    n3=0.000001
    for a in arr:
        if a > 0:
            n1+=1
        elif a < 0:
            n2+=1
        elif a==0:
            n3+=1
         
    print(n1/len(arr))
    print(n2/len(arr))
    print(n3/len(arr))
    