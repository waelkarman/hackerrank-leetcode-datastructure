
def breakingRecords(scores):
    # Write your code here
    w_min=scores[0]
    w_max=scores[0]
    max_break_record=0
    min_break_record=0
    back=scores[0]
    i=-1
    for a in scores:
        i+=1
        if a > w_max:
            w_max=a
            max_break_record += 1
                
        if a < w_min:
            w_min=a
            min_break_record +=1
        back=a
    return [max_break_record,min_break_record]
            
