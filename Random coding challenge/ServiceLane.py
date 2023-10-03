def serviceLane(width, cases):
    # Write your code here
    result = []
    for c in cases:
        min_val=width[c[0]:c[1]+1][0]
        for e in width[c[0]:c[1]+1]:
            if( e < min_val ):
                min_val=e
        result.append(min_val)
    return result
