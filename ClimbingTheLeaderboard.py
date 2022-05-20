

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


