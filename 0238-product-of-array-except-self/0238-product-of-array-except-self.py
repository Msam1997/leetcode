class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[1 for _ in nums]
        l=1
        r=1
        for i in range(len(nums)):
            a[i]*=l
            a[-1-i]*=r
            l*=nums[i]
            r*=nums[-1-i]
        return a

        
