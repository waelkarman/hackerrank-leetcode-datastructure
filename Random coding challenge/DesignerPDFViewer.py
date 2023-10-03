


def designerPdfViewer(h, word):
    # Write your code here
    ma=0
    for a in word:
        if a=='a':
            n=0
            
        if a=='b':
            n=1
            
        if a=='c':
            n=2
            
        if a=='d':
            n=3
            
        if a=='e':
            n=4
            
        if a=='f':
            n=5
            
        if a=='g':
            n=6
            
        if a=='h':
            n=7
            
        if a=='i':
            n=8
            
        if a=='j':
            n=9
            
        if a=='k':
            n=10
            
        if a=='l':
            n=11
            
        if a=='m':
            n=12
            
        if a=='n':
            n=13
            
        if a=='o':
            n=14
            
        if a=='p':
            n=15                                                                                              
        if a=='q':
            n=16 
        
        if a=='r':
            n=17 
            
        if a=='s':
            n=18                                                                                                  
        if a=='t':
            n=19                    
        
        if a=='u':
            n=20 
            
        if a=='v':
            n=21             
            
        if a=='w':
            n=22 
            
        if a=='x':
            n=23 
            
        if a=='y':
            n=24                                 
            
        if a=='z':
            n=25            
        
        if h[n]>ma:
            ma = h[n]
        
    return len(word)*ma


