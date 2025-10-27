# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。 
# 
#  字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而
# "aec"不是）。 
# 
#  进阶： 
# 
#  如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代
# 码？ 
# 
#  致谢： 
# 
#  特别感谢 @pbrother 添加此问题并且创建所有测试用例。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abc", t = "ahbgdc"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "axc", t = "ahbgdc"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 100 
#  0 <= t.length <= 10^4 
#  两个字符串都只由小写字符组成。 
#  
# 
#  Related Topics 双指针 字符串 动态规划 👍 1202 👎 0
from debugpy.common.timestamp import current


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isSubsequence(self, substr: str, fullstr: str) -> bool:
        current_index, index_len = 0, len(fullstr)
        older_index = -1
        for ch in substr:
            while current_index < index_len and fullstr[current_index] != ch:
                current_index += 1
            # 1.到最后都没发现ch 2.当前ch对应的索引比上一个ch对应的索引小
            if current_index == index_len or current_index < older_index:
                return False
            older_index = current_index
            current_index += 1
        return True
        
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    bb = s.isSubsequence("axc", "ahbgdc")
    print(bb)