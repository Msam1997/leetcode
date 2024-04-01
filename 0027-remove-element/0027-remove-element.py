class Solution(object):
    def removeElement(self, num, val):
        k=0
        for i in range(len(num)):
            if num[i]!= val:
                num[k]=num[i]
                k+=1
        return k
        
        








