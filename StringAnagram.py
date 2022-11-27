def stringAnagram(dictionary, query):
    # Write your code here   
        
    l=[]
    anagram = True
    for ques in query:
        count=0
        for dicts in dictionary:
            anagram = True
            for q in ques:
                if( ques.count(q) != dicts.count(q) ):
                    anagram = False
            if(anagram):
                count+=1
        l.append(count)
    return l
