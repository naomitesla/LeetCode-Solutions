class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            remainder = target - i  
            try:
                pos_1 = int(nums.index(i))
                pos_2 = int(nums.index(remainder, pos_1+1))
            except:
                continue
            return "{0}{1}".format(pos_1, pos_2)