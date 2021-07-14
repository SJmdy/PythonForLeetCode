# 使用链表解决的问题

from src import common


from .common import ListNode


# 92. 反转链表 II
#
# 给你单链表的头节点 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
#
# LC: [92. 反转链表 II](https://leetcode-cn.com/problems/reverse-linked-list-ii/)
def reverse_between(head: ListNode, left: int, right: int) -> ListNode:
    if head is None or left == right:
        return head

    left, right = left - 1, right - 1

    cur = head
    for _ in range(0, right):
        cur = cur.next
    third_half = cur.next
    print(common.ListNode.serialize(head=third_half))

    if left == 0:
        slow_cur = None
        fast_cur = head
        for _ in range(0, right - left + 1):
            print("fc: ", fast_cur.val)
            next = fast_cur.next
            fast_cur.next = slow_cur
            slow_cur = fast_cur
            fast_cur = next

        cur = slow_cur
        while cur.next is not None:
            cur = cur.next
        cur.next = third_half
        return slow_cur
    else:
        cur = head
        for _ in range(0, left - 1):
            cur = cur.next

        slow_cur = None
        fast_cur = cur.next

        for _ in range(0, right - left + 1):
            next = fast_cur.next
            fast_cur.next = slow_cur
            slow_cur = fast_cur
            fast_cur = next
        cur.next = slow_cur

        cur = slow_cur
        while cur.next is not None:
            cur = cur.next
        cur.next = third_half
        return head


# 82. 删除排序链表中的重复元素 II
#
# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
#
# 返回同样按升序排列的结果链表。
#
# LC: [82. 删除排序链表中的重复元素 II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/)
def delete_duplicates2(head: ListNode) -> ListNode:
    if head is None:
        return None

    new_head = ListNode(val=-1)
    new_head.next = head

    cur = head
    prev_cur = new_head

    while cur is not None:
        next = cur.next
        if next is None:
            break

        if cur.val == next.val:
            next_cur = next
            while next_cur is not None and next_cur.val == cur.val:
                next_cur = next_cur.next
            prev_cur.next = next_cur
            cur = next_cur
        else:
            prev_cur = cur
            cur = next
    return new_head.next


# 83. 删除排序链表中的重复元素
#
# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
#
# 返回同样按升序排列的结果链表。
# LC: [83. 删除排序链表中的重复元素](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/)
def delete_duplicates1(head: ListNode) -> ListNode:
    if head is None:
        return head
    cur = head

    while cur is not None:
        next = cur.next
        if next is None:
            break
        if cur.val == next.val:
            next_cur = next
            while next_cur is not None and next_cur.val == cur.val:
                next_cur = next_cur.next
            cur.next = next_cur
            cur = cur.next
        else:
            cur = next
    return head

