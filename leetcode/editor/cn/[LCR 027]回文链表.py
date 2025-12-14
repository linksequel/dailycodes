# 给定一个链表的 头节点 head ，请判断其是否为回文链表。 
# 
#  如果一个链表是回文，那么链表节点序列从前往后看和从后往前看是相同的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入: head = [1,2,3,3,2,1]
# 输出: true 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入: head = [1,2]
# 输出: false
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表 L 的长度范围为 [1, 10⁵] 
#  0 <= node.val <= 9 
#  
# 
#  
# 
#  进阶：能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
# 
#  
# 
#  
#  注意：本题与主站 234 题相同：https://leetcode-cn.com/problems/palindrome-linked-list/ 
# 
#  Related Topics 栈 递归 链表 双指针 👍 147 👎 0
from typing import Optional, List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev, cur = None, head
        val_list:List[int] = []
        while cur:
            val_list.append(cur.val)
            tmp_next = cur.next
            cur.next = prev

            prev = cur
            cur = tmp_next

        # get reverse start from prev
        if not val_list or not prev:
            return False
        return val_list == val_list[::-1]
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    s.isPalindrome(head)