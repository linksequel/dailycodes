# 给定一个含有 n 个正整数的数组和一个正整数 target 。 
# 
#  找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其
# 长度。如果不存在符合条件的子数组，返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
#  
# 
#  示例 2： 
# 
#  
# 输入：target = 4, nums = [1,4,4]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= target <= 10⁹ 
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁴ 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。 
#  
# 
#  Related Topics 数组 二分查找 前缀和 滑动窗口 👍 2537 👎 0
import unittest
from itertools import accumulate
from typing import List



# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        init_len = len(nums)
        startp, endp = 0, 0
        accumulate = 0
        min_sub = init_len + 1
        while endp < init_len:
            accumulate += nums[endp]
            while accumulate >= target:
                min_sub = min(min_sub, endp - startp + 1)
                accumulate -= nums[startp]
                startp += 1
            endp += 1
        return 0 if min_sub == init_len + 1 else min_sub

    #超过时间限制
    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        if any(num >= target for num in nums):
            return 1
        for size in range(2, len(nums) + 1):
           if self.judge_n_windows_satisfy(target, size-1, nums):
               return size
        return 0

    def judge_n_windows_satisfy(self, target:int, size:int, nums: List[int]) ->  bool:
        startp, endp = 0, size
        while endp < len(nums):
            if sum(nums[startp:endp+1]) >= target:
                return True
            startp += 1
            endp += 1
        return False

# leetcode submit region end(Prohibit modification and deletion)
class TestMinSubArrayLen(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """测试示例 1: target = 7, nums = [2,3,1,2,4,3]"""
        target = 11
        nums = [1,2,3,4,5]
        expected = 3
        result = self.solution.minSubArrayLen(target, nums)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()