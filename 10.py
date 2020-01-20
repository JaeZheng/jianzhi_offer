"""
题目描述:
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

解决思路:
本质还是斐波那契额数列
链接：https://www.nowcoder.com/questionTerminal/72a5a919508a4251859fb2cfb987a0e6?answerType=1&f=discussion
来源：牛客网
特殊的target=0时输出0，其他时候还是斐波那契递归。
一个2*n的矩形，可以分为两种方式填充
1、2*(n-1)  + 2*1 ，此时只要把RectCover(n-1)的那种，再拼接一个竖的2*1的就可以了，方法数目为RectCover(n-1)
2、2*(n-1) + 2*2，此时2*2可以看成横着放两个1*2，或者竖着放两个2*1，但是其中竖的的正好是方法1的方式，故只算上横的即可，方法数目为RectCover（n-2）
"""

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number <= 2:
            return number
        ans = [0 for _ in range(number + 1)]
        ans[1] = 1
        ans[2] = 2
        for i in range(3,number+1):
            ans[i] = ans[i-1] + ans[i-2]
        return ans[-1]