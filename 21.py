"""
题目描述:
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）
解决思路：
用一个辅助栈，遍历压入顺序的数组，如果压入时栈的最后一个值与弹出序列的当前第一个值相等，则弹出。
遍历到最后，如果辅助栈为空，则说明压入和弹出顺序可以对应。
"""

# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        ptr = 0
        stack = []
        for i in range(0, len(pushV)):
            stack.append(pushV[i])
            while len(stack)!=0 and stack[-1]==popV[ptr]:
                stack.pop()
                ptr += 1
        return len(stack)==0

S = Solution()
pushV = [1,2,3,4,5]
popV = [4,3,5,1,2]
result = S.IsPopOrder(pushV, popV)
print(result)