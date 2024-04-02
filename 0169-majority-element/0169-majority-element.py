class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}
        max_freq = 0
        res = None
        
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter[num] > max_freq:
                max_freq = counter[num]
                res = num
                
        return res