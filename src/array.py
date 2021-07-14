# 数组类型的问题

from typing import List


# 1047. 删除字符串中的所有相邻重复项
#
# 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。在 S 上反复执行重复项删除操作，直到无法继续删除。在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
#
# LC: [1047. 删除字符串中的所有相邻重复项](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/)
def remove_duplicates(s: str) -> str:
    if len(s) == 0:
        return s

    left_cur = 0
    right_cur = 1
    mask = [False for _ in range(0, len(s))]

    while right_cur < len(s):
        if s[left_cur] != s[right_cur]:
            left_cur += 1
            right_cur += 1
        else:
            mask[left_cur] = True
            mask[right_cur] = True
            left_cur = right_cur + 1
            right_cur = left_cur + 1

    new_s = [s[i] if not mask[i] else "" for i in range(0, len(s))]

    if True not in mask:
        return "".join(new_s)
    else:
        return remove_duplicates(s="".join(new_s))


# 54. 螺旋矩阵
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
def spiral_order(matrix: List[List[int]]) -> List[int]:
    if len(matrix) == 0:
        return []

    # write code here
    row = len(matrix)
    col = len(matrix[0])
    num_layers = (min(row, col) + 1) // 2
    layer = 0
    res = []

    while layer < num_layers:
        print("layer: ", layer)
        # (layer, layer)[包含] -> (layer, col - layer - 1)[包含]
        for i in range(layer, col - layer):
            res.append(matrix[layer][i])

        # (layer, col - layer - 1)[不包含] -> (row - layer - 1, col - layer - 1) [包含]
        for i in range(layer + 1, row - layer):
            res.append(matrix[i][col - layer - 1])

        # (row - layer - 1, col - layer - 1)[不包含] -> (row - layer - 1, layer)[不包含]
        if row - layer - 1 == layer:
            break
        for i in range(col - layer - 2, layer, -1):
            res.append(matrix[row - layer - 1][i])

        # (row - layer - 1, layer) [包含] -> (layer, layer)[不包含]
        if layer == col - layer - 1:
            break
        for i in range(row - layer - 1, layer, -1):
            res.append(matrix[i][layer])
        layer += 1
    return res


# 74. 搜索二维矩阵
#
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
# 每行中的整数从左到右按升序排列。
#
# 每行的第一个整数大于前一行的最后一个整数。
#
# LC: [74. 搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/)
def search_matrix(matrix: List[List[int]], target: int) -> bool:
    if len(matrix) == 0:
        return False

    m = len(matrix)
    n = len(matrix[0])

    if target < matrix[0][0] or target > matrix[-1][-1]:
        return False

    row = -1
    for i in range(0, m):
        if matrix[i][0] <= target:
            if matrix[i][0] == target:
                return True
            if i == m - 1 or matrix[i + 1][0] > target:
                row = i
                break

    if row == -1:
        return False

    for v in matrix[row]:
        if v == target:
            return True
    return False
