from src import dp
from src import array
from src import common
from src import recursion
from src import list_or_tree
from src import stack_or_queue
from src import written_test_coillect

if __name__ == '__main__':
    # 131. 分割回文串
    s = "asasab"
    r = recursion.partition(s=s)
    print("r: ", r)

    # 132. 分割回文串II
    s = "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"
    r = dp.min_cut(s=s)
    print("r: ", r)

    # 1047. 删除字符串中的所有相邻重复项
    s = "aaaaa"
    # 注：非最佳解法
    _ = array.remove_duplicates(s=s)
    r = stack_or_queue.remove_duplicates(s=s)
    print("r: ", r)

    # 224. 基本计算器
    s = "(1+(4+5+2)-3)-(6+8)"
    _ = recursion.calculate(s=s)
    r = stack_or_queue.calculate(s=s)
    print("r: ", r)

    # 227. 基本计算器 II [✔]
    s = "0-2147483647"
    r = stack_or_queue.calculate_2(s=s)
    print("r: ", r)

    # 912. 排序数组 [快速排序]
    nums = [3, 2, 2, 2, 1, 2, 1]
    res = written_test_coillect.sort_array(nums=nums)
    print("res: ", res)

    # 144. 二叉树的前序遍历
    tree = [1, None, 2, 3]
    tree = common.TreeNode.deserialize(data=tree)
    res = written_test_coillect.preorder_traversal(root=tree)
    print(res)

    # 92. 反转链表 II
    nums = [1, 2, 3, 4]
    tree = common.ListNode.deserialize(nums=nums)
    res = list_or_tree.reverse_between(head=tree, left=1, right=1)
    print("res: ", common.ListNode.serialize(head=res))

    # 82. 删除排序链表中的重复元素 II
    head = common.ListNode.deserialize([1, 1, 1, 2, 3])
    head = list_or_tree.delete_duplicates2(head=head)
    res = common.ListNode.serialize(head=head)
    print("res: ", res)

    # 83. 删除排序链表中的重复元素
    head = common.ListNode.deserialize([1, 1, 2])
    head = list_or_tree.delete_duplicates1(head=head)
    res = common.ListNode.serialize(head=head)
    print("res: ", res)

    # 54. 螺旋矩阵
    matrix = [[2, 5, 8], [4, 0, -1]]
    r = array.spiral_order(matrix=matrix)
    print(r)
