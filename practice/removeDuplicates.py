# wrong answer


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if (len(nums) == 0):
            print 0
        else:

            for j in range(0, len(nums)-1):
                if nums[j+1] != nums[j]:
                    i += 1
                    nums[j] = nums[j+1]
                    j += 1
            print i+1

Sol= Solution()
Sol.removeDuplicates([1,1,2,3,4,5])


# correct answer
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if (len(nums) == 0):
            return 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1