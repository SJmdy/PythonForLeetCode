from typing import List

# 131. 分割回文串
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。返回 s 所有可能的分割方案。
#
# LC: [131. 分割回文串](https://leetcode-cn.com/problems/palindrome-partitioning/solution/hui-su-you-hua-jia-liao-dong-tai-gui-hua-by-liweiw/
#
# 解题思路：回溯剪枝 [✔] 动态规划 []
#
# 从当前的字符串s开始，若s[..i]是回文串，则将s加入到path中去，并继续对剩下的字符串s[i..]进行分割
# 当当前字符串s为空时，将path加入到res中去。
def partition(s: str) -> List[List[str]]:
    def dfs(s: str, path: List[str], res: List[List[str]]):
        if len(s) == 0:
            res.append(path)
            return

        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                dfs(s=s[i:], path=path + [s[:i]], res=res)

    res = []
    dfs(s=s, path=[], res=res)
    return res


# 132. 分割回文串 II [✔]
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。返回符合要求的 最少分割次数 。
#
# LC: [132. 分割回文串 II](https://leetcode-cn.com/problems/palindrome-partitioning-ii/)
#
# 解题思路：回溯剪枝 [✔] | 动态规划 []
# 注意：超时
def min_cut(s: str) -> int:
    def dfs(s: str) -> int:
        if len(s) < 2 or s == s[::-1]:
            return 0
        times = []
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1]:
                times.append(dfs(s=s[i:]))
        return 1 + min(times)
    return dfs(s=s)


# 224. 基本计算器
#
# 实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。
#
# 注：'s' must consist of values in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '(', ')', ' '] only
#
# LC: [224. 基本计算器](https://leetcode-cn.com/problems/basic-calculator/)
#
# 解题思路：递归求解 [✔] | 栈
# 超时
def calculate(s: str) -> int:
    def calcu(s: str) -> int:
        if len(s) == 0:
            return 0
        nums = []
        ops = []

        if s.startswith('+') or s.startswith('-'):
            nums.append(0)

        left_cur = 0

        while left_cur < len(s):
            if s[left_cur] == '+':
                ops.append(True)
                left_cur += 1
            elif s[left_cur] == '-':
                ops.append(False)
                left_cur += 1
            elif s[left_cur] == '(':
                stack = ['(']
                bracket_cur = left_cur + 1

                while bracket_cur < len(s):
                    if s[bracket_cur] == '(':
                        stack.append('(')
                    elif s[bracket_cur] == ')':
                        stack.pop()
                    if len(stack) == 0:
                        break
                    bracket_cur += 1
                nums.append(calcu(s=s[left_cur + 1: bracket_cur]))
                left_cur = bracket_cur + 1
            elif s[left_cur] == ')':
                left_cur += 1
            else:
                # 是数字
                digit_cur = left_cur + 1
                while digit_cur < len(s) and s[digit_cur].isdigit():
                    digit_cur += 1
                digit = int(s[left_cur: digit_cur])
                nums.append(digit)
                left_cur = digit_cur
        res = nums[0]
        for (idx, op) in enumerate(ops):
            if op:
                res += nums[idx + 1]
            else:
                res -= nums[idx + 1]
        return res
    s = s.replace(" ", "")
    return calcu(s=s)



