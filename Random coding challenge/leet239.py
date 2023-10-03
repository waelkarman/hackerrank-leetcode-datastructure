# #################################### SOLUTION 0 #58
nums = [1,3,-1,-3,5,3,6,7]
k = 3

out = []
maxlist = [None] * k
i=0

back=0
front=k
first=True
maxval = nums[0]
for n in nums:
    pos = i % k
    maxlist[pos]=n

    if(i>=k-1):
        if(first or nums[back] == maxval):
            maxval = maxlist[0]
            for a in maxlist:    
                if(a > maxval):
                    maxval=a
            out.append(maxval)
            if(not first):
                back+=1
                front+=1
            first=False
        else:
            if(nums[front] > maxval):
                out.append(nums[front])
                maxval=nums[front]
            elif(k==1):
                out.append(n)
                maxval = n
            else:
                out.append(maxval)
            back+=1
            front+=1
    i+=1
    

print(out)


# #################################### SOLUTION 0 #45
# out = []
# maxlist = [None] * k
# i=0
# for n in nums:
#     pos = i % k
#     maxlist[pos]=n
#     maxval = maxlist[0]

#     if(i>=k-1):
#         for a in maxlist:
#             if(a > maxval):
#                 maxval=a
#         out.append(maxval)
#     i+=1  