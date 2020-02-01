"""
题目描述:
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
解决思路：
字典存储所有数字，遍历数字，如果出现超过数组长度的一半的数字，返回该数字。否则返回0。
"""

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        num_set = set(numbers)
        length = len(numbers)
        if length == 0:
            return 0
        for i in num_set:
            if numbers.count(i) > length/2:
                return i
        return 0


numbers = [1,2,3,2,2,2,5,4,1]
S = Solution()
result = S.MoreThanHalfNum_Solution(numbers)
print(result)