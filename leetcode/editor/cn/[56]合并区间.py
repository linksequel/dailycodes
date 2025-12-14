# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返
# 回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  
# 
#  示例 2： 
# 
#  
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。 
# 
#  示例 3： 
# 
#  
# 输入：intervals = [[4,7],[1,4]]
# 输出：[[1,7]]
# 解释：区间 [1,4] 和 [4,7] 可被视为重叠区间。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= intervals.length <= 10⁴ 
#  intervals[i].length == 2 
#  0 <= starti <= endi <= 10⁴ 
#  
# 
#  Related Topics 数组 排序 👍 2667 👎 0

from typing import List
import bisect

from sympy.physics.units import length


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

    def merge_myself(self, intervals: List[List[int]]) -> List[List[int]]:
        my_dict = {}
        for interval in intervals:
            self.map_interval2dict(interval, my_dict)
        return self.map_dict2intervals(my_dict)

    def map_interval2dict(self, interval:List[int], my_dict:dict[int, str]) -> None:
        if len(interval) < 2:
            return
        if interval[0] == interval[1]:
            if interval[0] not in my_dict:
                my_dict[interval[0]] = 'o'
            return
        for num in range(interval[0], interval[1] + 1):
            if num == interval[0]:
                # 已经存在，
                if num in my_dict:
                    # 只有相同才保留，如[1,4],[1,4] 其他情况全换成空
                    if my_dict[num] == '[' or my_dict[num] == 'o':
                        my_dict[num] = '['
                    else:
                        my_dict[num] = ''
                else:
                    my_dict[num] = '['
            elif num == interval[1]:
                # 已经存在
                if num in my_dict:
                    # 只有相同才保留，如[1,4],[1,4] 其他情况全换成空
                    if my_dict[num] == ']' or my_dict[num] == 'o':
                        my_dict[num] = ']'
                    else:
                        my_dict[num] = ''
                else:
                    my_dict[num] = ']'
            else:
                my_dict[num] = ''

    def to_find_symbol(self, cur_idx:int, symbol:str, my_dict, sortd_keys) -> int:
        in_len = len(sortd_keys)
        while cur_idx < in_len and my_dict[sortd_keys[cur_idx]] != symbol:
            cur_idx += 1
        return cur_idx

    def map_dict2intervals(self, my_dict:dict[int, str]):
        res =  []
        sortd_keys = sorted(my_dict.keys())
        idx, length = 0, len(sortd_keys)
        while idx < length:
            if my_dict[sortd_keys[idx]] == 'o':
                res.append([sortd_keys[idx]]*2)
                idx += 1
                continue
            # To find [
            idx = self.to_find_symbol(idx, '[', my_dict, sortd_keys)
            if idx == length:
                break
            # Found [
            interval_start = sortd_keys[idx]
            # To find ]
            idx += 1
            idx = self.to_find_symbol(idx, ']', my_dict, sortd_keys)
            if idx == length:
                break
            # Found ]
            interval_end = sortd_keys[idx]
            res.append([interval_start, interval_end])
            # To next
            idx += 1

        return res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    #merge = s.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    merge = s.merge([[0,2],[2,3],[4,4],[0,1],[5,7],[4,5],[0,0]])
    print(merge)