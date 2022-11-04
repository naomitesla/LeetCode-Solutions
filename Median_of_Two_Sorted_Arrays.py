# Naomi Tesla
# https://leetcode.com/problems/median-of-two-sorted-arrays/

import math

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sorted_l = nums1 + nums2
        sorted_l.sort()
        length = len(sorted_l)

        if length%2 == 0:
            crossed = (length - 2)/2
            first_index = sorted_l[crossed]
            last_index = sorted_l[crossed+1]
            result = float(first_index + last_index)/2
        else:
            result = sorted_l[int(math.ceil(length/2))]
    
        return result

    