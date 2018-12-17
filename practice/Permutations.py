class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        n = len(nums)

        for num in nums:
            new_res = []
            for i in range(len(res)):
                prev = res[i]
                prev.append(num)
                for j in range(len(prev)):
                    prev[j], prev[-1] = prev[-1], prev[j]
                    new_res.append(prev[:])
                    prev[j], prev[-1] = prev[-1], prev[j]
            res = new_res
        return res


sol = Solution()
nums=[1,2,3]
print sol.permute(nums)





