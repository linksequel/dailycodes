#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
import unittest
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = []
        for index in range(len(prices) -1 ):
            sub = max(prices[index+1:]) - prices[index]
            print("current num is %d, sub is %d" % (prices[index], sub ))
            if (sub < 0):
                continue
            else:
                res.append(sub)
        return sum(res)

if __name__ == '__main__':
    solution = Solution()
    prices = [7,1,5,3,6,4]
    print(solution.maxProfit(prices))

# @lc code=end

