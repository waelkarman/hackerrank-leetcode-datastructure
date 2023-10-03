
def timeConversion(s):
    # Write your code here
    print(f"AM - PM : {s[8]}")
    print(f"hour:{s[0]}{s[1]}")
    if(s[8]=='A'):
        if s[0] == '1' and s[1] == '2':
            print(f"One: ")
            return '00'+s[2:8]
            #s[0]='0'
            #s[1]='0'
            
    if(s[8]=='P'):
        if s[0] == '1' and s[1] == '2':
                print(f"Five: ")
                return '12'+s[2:8]
        if s[0] == '2' and s[1] == '4':
            print(f"Two: ")
            return '00'+s[2:8]
            #s[0]='0'
            #s[1]='0'
        else:
            a=int(s[0]+s[1])
            a=a+12
            a=str(a)
            if(len(a)==1):
                print(f"Three: ")
                return '0'+a+s[2:8]
                #s[0]='0'
                #s[1]=a
            else:
                print(f"Four: ")
                return a+s[2:8]
                #s[0]='0'
                #s[1]='0'
    
    return s[0:8]

