class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        helper = []
        for i in range(0,len(gas)):
            helper.append(gas[i]-cost[i])
        k=0
        sums=0
        count=0
        while k < 2*len(gas):
            index = k%len(gas)
            k+=1
            if count<len(gas):
                sums+=helper[index]
                if sums < 0:
                    count = -1
                    sums = 0
            else:
                return (k-1-count)%len(gas)
            count+=1
        return -1

        #SOLUTION A
        #init = -1
        #for s in range(0,len(gas)):
        #    status=0
        #    count=0
        #    if gas[s] >= cost[s]:
        #        i=s
        #        enter = True
        #        while enter or i != s:
        #            enter = False
        #            status += gas[i]
        #            #print(f"Verifico: {status} >= {cost[i]} ")
        #            if (status < cost[i]):
        #                break
        #            else:
        #                count+=1
        #            status -= cost[i]
        #            #print(f"I={i}, status:{status}")
        #            i=(i+1)%len(gas)
        #
        #
        #        if count == len(gas):
        #            init = s
        #            return init            
        #
        #return init
        