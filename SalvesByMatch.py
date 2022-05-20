
def sockMerchant(n, ar):
    # Write your code here
    n_pairs=0
    pairs={}
    for a in ar:
        pairs[a]=0
    for a in ar:
        pairs[a]+=1
    for a in pairs.keys():
        n_pairs+=int(pairs[a]/2)
        
    return n_pairs
        
