"""
题目描述:
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
解决思路：
两个额外数组，一个存奇数，一个存偶数，遍历后再拼接起来
"""

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        ji = []
        ou = []
        for i in array:
            if i%2 == 0:
                ou.append(i)
            else:
                ji.append(i)
        return ji+ou

S = Solution()
array = [1,4,3,5,2,6,7,9]
result = S.reOrderArray(array)
print(result)