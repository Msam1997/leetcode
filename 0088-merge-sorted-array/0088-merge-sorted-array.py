class Solution(object):
    def merge(self, nums1, m, nums2, n):
       l=m+n-1
       while m>0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[l] = nums1[m-1]
                m-=1
            else:
                nums1[l] = nums2[n-1]
                n-=1
            l-=1
    
       if n>0:
            nums1[:n] = nums2[:n]
            


        