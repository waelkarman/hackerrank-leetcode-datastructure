def acmTeam(topic):
    # Write your code here
    team=0
    max_count = 0 
    for t1 in range(len(topic)):
        for t2 in range(t1+1,len(topic)):
            count=0
            for i in range(len(topic[0])):
                if(topic[t1][i]=='1'  or topic[t2][i]=='1'):
                    count+=1
            if(count >= max_count):
                if(count == max_count):
                    team +=1 
                else:
                    team =1 
                max_count = count
    return [max_count,team]
