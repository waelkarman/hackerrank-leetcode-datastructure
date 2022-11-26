

def climbingLeaderboard(ranked, player):
    # Write your code here
    scores = []
    score=1
    i=0
    j=0
    
    while(i<len(player)):
        if player[len(player)-i-1]<ranked[j]:
            if j == 0:                    
                score+=1
            if j>0:
                if ranked[j-1]!=ranked[j]:
                    score+=1
            
            if j == (len(ranked)-1):
                while(i<len(player)):
                    scores.append(score)
                    i+=1
                break
            else:
                j+=1    
        else:
            scores.append(score) 
            i+=1
   
    scores.reverse()            
    return scores

    #scores = []
    #back_a = None
    #first = True
#
#
    ##k = {}    
    ##for a in ranked:
    ##    k[a] = 0
    #
    #for p in player:
    #    score = 1
    #    for a in ranked:
    #        if (p < a) and ((back_a is not None and a != back_a) or (first)):
    #            first = False
    #            score+=1
    #        back_a=a
    #    scores.append(score)
    #return scores

   #def climbingLeaderboard(ranked, player):
#    # Write your code here
#
#    results = []
#    first = True
#    
#    #player = [5]
#    for p in player:    
#        temp = 0
#        count = 1
#        for s in ranked:
#            #print(f"---p : {p}  and r : {s}   and count : {count}, temp : {temp}, count : {count}")
#            if( p<s ):
#                if( s != temp ):
#                    count += 1
#                    temp = s
#                first = False
#            else:
#                #print(f"---p : {p}  and r : {s}  ")
#                if(first):
#                    first = False
#                    results.append(1)
#                    #print("APPENDED0")
#                    temp = s
#                    break
#                else:
#                    results.append(count)
#                    #print("APPENDED1")
#                    temp = s
#                    break
#            
#        if( p<ranked[len(ranked)-1] ):
#            results.append(count)
#            
#        
#    return results
#     
