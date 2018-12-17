__author__ = 'Administrator'
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x <= 0:
            return False

        temp = x
        rev = 0
        while(temp > 0):
            rev = rev*10+temp%10
            temp /= 10
        return rev == x

s = Solution()
x = input()
print s.isPalindrome(x)



