# 笔试（包括面试中的笔试）遇到的题

from typing import List
from typing import Dict
from .common import TreeNode
from .common import ListNode


# 912. 排序数组 [快速排序]
#
# 给你一个整数数组 nums，请你将该数组升序排列
#
# LC: [912. 排序数组（快速排序）](https://leetcode-cn.com/problems/sort-an-array/)
def sort_array(nums: List[int]) -> List[int]:
    if len(nums) < 2:
        return nums

    def quick_sort(nums: List[int], start: int, end: int):
        if start >= end or start >= len(nums):
            return

        pivot = nums[start]
        left_cur, right_cur = start, end

        while left_cur < right_cur:
            while left_cur < right_cur and nums[right_cur] > pivot:
                right_cur -= 1
            while left_cur < right_cur and nums[left_cur] <= pivot:
                left_cur += 1
            nums[left_cur], nums[right_cur] = nums[right_cur], nums[left_cur]
        nums[start], nums[left_cur] = nums[left_cur], nums[start]

        if left_cur > 0:
            quick_sort(nums=nums, start=start, end=left_cur - 1)
        quick_sort(nums=nums, start=left_cur + 1, end=end)

    quick_sort(nums=nums, start=0, end=len(nums) - 1)
    return nums


# 72. 编辑距离
#
# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：插入一个字符、删除一个字符、替换一个字符
#
# LC: [编辑距离](https://leetcode-cn.com/problems/edit-distance/)
def min_distance(word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)
    if m == 0:
        return n
    if n == 0:
        return m

    dp = [[0 for _ in range(0, n + 1)] for _ in range(0, m + 1)]
    for i in range(1, m + 1):
        dp[i][0] = i
    for i in range(1, n + 1):
        dp[0][i] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # dp[i][j - 1] + 1: 在 s1 的末尾添加一个字符
                # dp[i - 1][j] + 1: 在 s2 的末尾添加一个字符
                # dp[i - 1][j - 1] + 1: 修改 s1 的末尾字符使之变为 s2的末尾字符
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
    return dp[m][n]


# 144. 二叉树的前序遍历
#
# LC: [144. 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)
def preorder_traversal(root: TreeNode) -> List[int]:
    if root is None:
        return []
    cursor = root
    stack = [cursor]
    res = []

    while len(stack) > 0:
        cursor = stack.pop()
        res.append(cursor.val)
        if cursor.right is not None:
            stack.append(cursor.right)
        if cursor.left is not None:
            stack.append(cursor.left)
    return res


# 94. 二叉树的中序遍历
#
# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
#
# LC: [94. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)
def inorder_traversal(root: TreeNode) -> List[int]:
    if root is None:
        return []

    stack = []
    cursor = root
    res = []

    while len(stack) > 0 or cursor is not None:
        while cursor is not None:
            stack.append(cursor)
            cursor = cursor.left
        cursor = stack.pop()
        res.append(cursor.val)
        cursor = cursor.right
    return res


# 145. 二叉树的后序遍历
#
# 给定一个二叉树，返回它的 后序 遍历。
#
# LC: [145. 二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)
def postorder_traversal(root: TreeNode) -> List[int]:
    if root is None:
        return []

    cursor = root
    stack = [cursor]
    res = []

    while len(stack) > 0:
        cursor = stack.pop()
        res.append(cursor.val)

        if cursor.left is not None:
            stack.append(cursor.left)
        if cursor.right is not None:
            stack.append(cursor.right)
    res.reverse()
    return res


# 300. 最长递增子序列 [✔]
#
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
#
# LC: [300. 最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/)
#
# 解题思路：动态规划
#
# dp[i]: 以**nums[i]为结尾字符**的最长严格递增子序列的长度。
#
# 则有：
#
# dp[i] = max(dp[j]) + 1, 0 <= j < i and nums[j] < nums[i]
def length_of_lis(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    dp = [1 for _ in range(0, len(nums))]

    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)