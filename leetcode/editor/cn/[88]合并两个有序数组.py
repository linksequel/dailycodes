# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。 
# 
#  请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。 
# 
#  注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并
# 的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 解释：需要合并 [1,2,3] 和 [2,5,6] 。
# 合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
# 解释：需要合并 [1] 和 [] 。
# 合并结果是 [1] 。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums1 = [0], m = 0, nums2 = [1], n = 1
# 输出：[1]
# 解释：需要合并的数组是 [] 和 [1] 。
# 合并结果是 [1] 。
# 注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums1.length == m + n 
#  nums2.length == n 
#  0 <= m, n <= 200 
#  1 <= m + n <= 200 
#  -10⁹ <= nums1[i], nums2[j] <= 10⁹ 
#  
# 
#  
# 
#  进阶：你可以设计实现一个时间复杂度为 O(m + n) 的算法解决此问题吗？ 
# 
#  Related Topics 数组 双指针 排序 👍 2858 👎 0
import unittest
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = m - 1, n - 1
        last = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[last] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[last] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[last] = nums1[p1]
                p1 -= 1
            elif nums1[p1] <= nums2[p2]:
                nums1[last] = nums2[p2]
                p2 -= 1
            last -= 1

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        if m != 0 and n == 0:
            return
        if m == 0 and n != 0:
            nums1[:] = nums2
            return

        result = []
        point_num1 : int = 0
        point_num2 : int = 0

        while len(result) < m + n:
            if point_num1 < m and point_num2 < n:
                if nums1[point_num1] <= nums2[point_num2]:
                    result.append(nums1[point_num1])
                    point_num1 += 1

                elif nums1[point_num1] > nums2[point_num2]:
                    result.append(nums2[point_num2])
                    point_num2 += 1

            elif point_num1 == m:
                while point_num2 < n:
                    result.append(nums2[point_num2])
                    point_num2 += 1

            elif point_num2 == n:
                while point_num1 < m:
                    result.append(nums1[point_num1])
                    point_num1 += 1
        nums1[:] = result
# leetcode submit region end(Prohibit modification and deletion)


class TestMerge(unittest.TestCase):

    def setUp(self):
        """在每个测试方法之前运行"""
        self.solution = Solution()

    def test_example1(self):
        """测试示例1: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3"""
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        expected = [1,2,2,3,5,6]

        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)


if __name__ == '__main__':
    unittest.main()
