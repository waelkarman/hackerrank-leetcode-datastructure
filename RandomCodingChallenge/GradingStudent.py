 
def gradingStudents(grades):
    # Write your code here
    collector = []
    for a in grades:
        col=a
        if a>37:
            b=int(a/5)
            print(a,"-",b)
            b+=1
            c=b*5
            print(c,'---')
            if(c-a)<3:
                col=c
            
        collector.append(col)
        
    return collector


