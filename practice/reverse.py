class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = []
        f = False
        if x < 0:
            x *= -1
            f = True
        while True:
            temp.append(x % 10)
            x /= 10
            if x == 0:
                break
        result = 0
        for i in temp:
            result = i + 10*result
        if f:
            result *= -1
        if result > 2147483647 or result<-2147483648:
            return 0
        print result

sol = Solution()
sol.reverse(-265)


