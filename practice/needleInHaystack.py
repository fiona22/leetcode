class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=="":
            print 0
        for i in range(haystack.__len__()):
            if haystack[i:i+needle.__len__()] == needle:
                print i
        if haystack.__contains__(needle)==0:
            print -1



sol = Solution()
sol.strStr("a", "a")

