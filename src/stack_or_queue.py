# 使用栈或队列解决的问题


# 1047. 删除字符串中的所有相邻重复项
#
# 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。在 S 上反复执行重复项删除操作，直到无法继续删除。在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
#
# LC: [1047. 删除字符串中的所有相邻重复项](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/)
def remove_duplicates(s: str) -> str:
    if len(s) == 0:
        return s

    stack = []
    for i in range(0, len(s)):
        if len(stack) == 0 or s[i] != stack[-1]:
            stack.append(s[i])
        else:
            stack.pop()
    return "".join(stack)


# 224. 基本计算器 [✔]
#
# 实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。
#
# 注：'s' must consist of values in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '(', ')', ' '] only
#
# LC: [224. 基本计算器](https://leetcode-cn.com/problems/basic-calculator/)
#
# 解题思路：递归求解 | 栈 [✔]
#
# op: 当前所应该进行的操作，+ 或 -
#
# ops: 栈，存放`()`外部的操作符，整体对`()`中的内容是 + 或 -。例如 `-(1 - (2 + 3))`，那么第一个括号对应的符号为
# `-`，第二个括号对应的符号为 `+`；对于任何公式`s`，都可以转化为`+(s)`的形式，因此ops初始化压入`+`。
#
# op具体为`+` 或 `-` 取决于ops栈顶符号和当前的操作符；若当前的符号为`'+'`，那么op与ops栈顶保持已知；否则，op为ops栈顶的
# 相反操作
def calculate(s: str) -> int:
    s = s.replace(' ', '')
    if len(s) == 0:
        return 0

    stack = [True]
    op = True

    left_cur = 0
    res = 0
    while left_cur < len(s):
        if s[left_cur] == '+':
            op = stack[-1]
            left_cur += 1
        elif s[left_cur] == '-':
            op = not stack[-1]
            left_cur += 1
        elif s[left_cur] == '(':
            stack.append(op)
            left_cur += 1
        elif s[left_cur] == ')':
            stack.pop()
            left_cur += 1
        else:
            # 数字
            digit_cur = left_cur + 1
            while digit_cur < len(s) and s[digit_cur].isdigit():
                digit_cur += 1
            digit = int(s[left_cur: digit_cur])
            if op:
                res += digit
            else:
                res -= digit
            left_cur = digit_cur
    return res


# 227. 基本计算器 II [✔]
#
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。整数除法仅保留整数部分。
#
# LC: [227. 基本计算器 II](https://leetcode-cn.com/problems/basic-calculator-ii/)
#
# 解题思路：栈
def calculate_2(s: str) -> int:
    s = s.replace(' ', '')

    if len(s) == 0:
        return 0

    def get_num(cur: int, s: str) -> (int, int):
        # 获取从 cur 起的数字；s[cur]是数字
        digit_cur = cur + 1
        while digit_cur < len(s) and s[digit_cur].isdigit():
            digit_cur += 1
        return int(s[cur: digit_cur]), digit_cur

    left_cur = 0
    flag = True
    calcu = []

    while left_cur < len(s):
        print("calcu: ", calcu)
        if s[left_cur] == '+':
            flag = True
            left_cur += 1
        elif s[left_cur] == '-':
            flag = False
            left_cur += 1
        elif s[left_cur] == '*':
            digit, digit_cur = get_num(cur=left_cur + 1, s=s)
            prev_digit = calcu.pop()
            calcu.append(prev_digit * digit)
            left_cur = digit_cur
        elif s[left_cur] == '/':
            digit, digit_cur = get_num(cur=left_cur + 1, s=s)
            prev_digit = calcu.pop()
            calcu.append(prev_digit // digit)
            left_cur = digit_cur
        else:
            digit, digit_cur = get_num(cur=left_cur, s=s)
            calcu.append(digit if flag else 0 - flag)
            left_cur = digit_cur
    return sum(calcu)