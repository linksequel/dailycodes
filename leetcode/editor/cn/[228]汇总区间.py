# 给定一个 无重复元素 的 有序 整数数组 nums 。 
# 
#  区间 [a,b] 是从 a 到 b（包含）的所有整数的集合。 
# 
#  返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个区间但不属于 
# nums 的数字 x 。 
# 
#  列表中的每个区间范围 [a,b] 应该按如下格式输出： 
# 
#  
#  "a->b" ，如果 a != b 
#  "a" ，如果 a == b 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [0,1,2,4,5,7]
# 输出：["0->2","4->5","7"]
# 解释：区间范围是：
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,2,3,4,6,8,9]
# 输出：["0","2->4","6","8->9"]
# 解释：区间范围是：
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 20 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  nums 中的所有值都 互不相同 
#  nums 按升序排列 
#  
# 
#  Related Topics 数组 👍 461 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        index_len = len(nums)
        result = []
        if index_len == 0:
            return result
        if index_len == 1:
            return [str(nums[0])]
        #demo input =  [0,1,2,4,5,7]
        index_start, index_end = 0, 1
        while index_end <= index_len :
            if index_start == index_len - 1:
                result.append(str(nums[index_start]))
                break

            if index_end == index_len:
                list2str = f"{nums[index_start]}->{nums[-1]}"
                result.append(list2str)
                break

            gap = index_end - index_start
            if nums[index_start] == nums[index_end] - gap:
                index_end += 1
            else:
                subset = nums[index_start:index_end]
                list2str = f"{subset[0]}->{subset[-1]}" if len(subset) > 1 else str(subset[0])
                result.append(list2str)
                # initialize
                index_start, index_end = index_end, index_end + 1

        return result

if __name__ == '__main__':
    s = Solution()
    res = s.summaryRanges([0,2,3,4,6,8,9])
    print(res)
# leetcode submit region end(Prohibit modification and deletion)
