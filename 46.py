"""
题目描述:
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。
其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。
每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,
继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。
请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
如果没有小朋友，请返回-1
解决思路：
第一种：约瑟夫环问题，套用递归公式
第二种：用链表或者数组模拟过程
"""

# -*- coding:utf-8 -*-
# 第一种
# import sys
# sys.setrecursionlimit(10000)  # 设置默认递归次数，系统默认为1000，有些大的数会超出递归次数
# class Solution:
#     def LastRemaining_Solution(self, n, m):
#         if n==0:
#             return -1
#         if n==1:
#             return 0
#         else:
#             return (self.LastRemaining_Solution(n-1, m)+m)%n


# 第二种
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n==0:
            return -1
        if n==1:
            return 0
        numbers = [i for i in range(n)]
        start = 0
        while len(numbers)>1:
            for i in range(1, m):
                start += 1
                if start == len(numbers):
                    start = 0
            numbers.remove(numbers[start])
            if start == len(numbers):
                start = 0
        return numbers.pop()


n, m = 4000, 997
S = Solution()
result = S.LastRemaining_Solution(n, m)
print(result)