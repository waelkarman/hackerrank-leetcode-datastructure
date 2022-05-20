

def pangrams(s):
    # Write your code here
    ma = {}
    s=s.lower()
    for a in s :
        ma[a]=0
    if len(ma) > 26:
        return "pangram"
    else:
        return "not pangram"


