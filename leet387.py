#
#   Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
#

class Solution:
    def firstUniqChar(self, s: str) -> int:
        single_list = {}
        index_list = {}
        min_value = len(s)
        r_val = s[0]
        i=0
        for c in s:
            if( c not in single_list):
                single_list[c] = 0
                index_list[c]=i
            else:
                single_list[c] += +1
            i+=1
        
        for c in single_list:
            if(single_list[c] < min_value):
                r_val=c
                min_value = single_list[c]

        if(min_value!=0):
            return -1
        
        return index_list[r_val]

a = Solution()

print(a.firstUniqChar("brodobrowd"))

