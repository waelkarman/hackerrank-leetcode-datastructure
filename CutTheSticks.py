

def cutTheSticks(arr):
    # Write your code here
    tot=[len(arr)]
    min_l=1001
    max_l=arr[0]
    repeat = True
    old_sum = 0
    old_min = 0
    while repeat:
        repeat = False
        for a in arr:
            #print(f"old_min:{old_min} min_l:{min_l}")
            if a > old_min and  a < min_l:
                min_l = a
                repeat = True
            if a > max_l:
                max_l = a
        #print(f"min_l: {min_l} --- arr.count(min_l) : {arr.count(min_l)}")
        tot.append(len(arr)-(arr.count(min_l)+old_sum))
        old_min = min_l
        old_sum += arr.count(min_l)
        min_l = 1001
        
        #print(tot) 
    return tot[0:len(tot)-2]
    

