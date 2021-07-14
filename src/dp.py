# 使用动态规划解决的问题

# 132. 分割回文串 II [✔]
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。返回符合要求的 最少分割次数 。
#
# LC: [132. 分割回文串 II](https://leetcode-cn.com/problems/palindrome-partitioning-ii/)
#
# 解题思路：回溯剪枝 [] | 动态规划 [✔]
#
# dp[i]: s[0..i + 1]的最小切割数
#
# dp[i] = 0 if 前i个字符是回文串
# dp[i] = min(dp[j]) + 1，其中s[j + 1..i]是回文串
#
# 使用is_partition辅助判断s[i..j + 1]是否是回文串
#
# is_partition[i][j] = (is_partition[i + 1][j - 1]) && s[i] == s[j]
def min_cut(s: str) -> int:
    if len(s) < 2 or s == s[::-1]:
        return 0

    dp = [0 for _ in range(0, len(s))]
    is_partition = [[False for _ in range(0, len(s))] for _ in range(0, len(s))]

    for i in range(0, len(s)):
        is_partition[i][i] = True

    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s)):
            if j == i + 1:
                is_partition[i][j] = s[i] == s[j]
            else:
                is_partition[i][j] = is_partition[i + 1][j - 1] and (s[i] == s[j])

    for i in range(1, len(s)):
        if is_partition[0][i]:
            dp[i] = 0
        else:
            min_cuts = 1e10
            for j in range(0, i):
                if is_partition[j + 1][i]:
                    if min_cuts > dp[j]:
                        min_cuts = dp[j]
            dp[i] = min_cuts + 1
    return dp[-1]
