from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return f"{self.name}-{self.score}"
        
    def comparator(a, b):
        ar=repr(a).split('-')
        br=repr(b).split('-')
        
        if  int(ar[1]) == int(br[1]):
            if ar[0] > br[0]:
                return 1
            else:
                return -1
        elif int(ar[1])<int(br[1]):
            return 1
        else:
            return -1
        
#n = int(input())
#data = []
#for i in range(n):
#    name, score = input().split()
#    score = int(score)
#    player = Player(name, score)
#    data.append(player)
#    
#data = sorted(data, key=cmp_to_key(Player.comparator))
#for i in data:
#    print(i.name, i.score)