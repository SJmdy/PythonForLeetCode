#
#
# @param matrix int整型二维数组
# @return int整型一维数组
#

def spiral_order(self, matrix):
    if len(matrix) == 0:
        return []

    # write code here
    row = len(matrix)
    col = len(matrix[0])
    num_layers = min(row, col) // 2 + 1
    layer = 0
    res = []

    while layer < num_layers:
        # 从(layer, layer)[包含]到(layer, col - layer - 1)[包含]
        # 左到右
        for i in range(layer, col - layer):
            res.append(matrix[layer][i])
        # 从(layer, col - layer - 1)[不包含] 到 (row - layer - 1, col - layer - 1) [包含]
        #
        for i in range(layer + 1, row - layer):
            res.append(matrix[i][col - layer - 1])
        # 从(row - layer - 1, col - layer - 1)[不包含]到(row - layer - 1, layer)[包含]
        if row - layer - 1 == layer:
            break
        for i in range(col - layer - 2, layer - 1, -1):
            res.append(matrix[row - layer - 1][i])
        #
        if layer == col - layer - 1:
            break
        for i in range(row - layer - 2, layer, -1):
            res.append(matrix[i][layer])
        layer += 1
    return res