"""
题目描述
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
 {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}，
 {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
"""

# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        if not num:
            return []
        if len(num) <= size:
            return max(num)
        result = []
        num_windows = len(num)-size+1
        for i in range(num_windows):
            result.append(max(num[i:i+size]))
        return result

num = [2,3,4,2,6,2,5,1]
size = 3
S = Solution()
result = S.maxInWindows(num, size)
print(result)