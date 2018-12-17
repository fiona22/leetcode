class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                print [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


sol = Solution()
sol.twoSum([3, 2, 4, 6, 7], 10)




