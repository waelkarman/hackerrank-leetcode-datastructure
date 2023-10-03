
def dayOfProgrammer(year):
    # Write your code here
    f=28
    mon=0
    i=0
    if year > 1918:
        if (year%4 == 0 and year%100 != 0) or year%400 == 0 :
            #is Julian leap year
            f=29
            
    if year < 1918:
        if year%4 == 0 :
            #leap year in Gregorian
            f=29
            
    if year == 1918:
        #if (year%4 == 0 and year%100 != 0) or year%400 == 0 :
            #is Julian leap year
        
        f=15
            
    print(f"thats f {f}")
    months = [31,f,31,30,31,30,31,31]
    

    for m in months:
        if mon < 256:
            mon+=m
            i+=1   
    d=256-mon
    i+=1
    if len(str(i))==1:
        i=f"0{i}"
    if len(str(d))==1:
        d=f"0{d}"
    return f"{d}.{i}.{year}"


