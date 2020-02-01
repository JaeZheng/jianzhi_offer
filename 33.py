"""
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
解决思路:
链接：https://www.nowcoder.com/questionTerminal/6aa9e04fc3794f68acf8778237ba065b?answerType=1&f=discussion
来源：牛客网
我们可以维护三个list，分别是乘2得到的丑数，乘3得到的丑数，乘5得到的丑数，但这样复杂度较高，而且会得到重复的丑数。
实际上每次我们只用比较3个数：用于乘2的最小的数、用于乘3的最小的数，用于乘5的最小的数。这样只需要维护三个指针，而不用维护三个数组。
"""

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        ugly_list = [1]
        p2, p3, p5 = 0, 0, 0
        for i in range(index-1):
            new_ugly = min(ugly_list[p2]*2, ugly_list[p3]*3, ugly_list[p5]*5)
            ugly_list.append(new_ugly)
            if new_ugly % 2 == 0:
                p2 += 1
            if new_ugly % 3 == 0:
                p3 += 1
            if new_ugly % 5 == 0:
                p5 += 1
        return ugly_list[-1]

index = 4
S = Solution()
result = S.GetUglyNumber_Solution(index)
print(result)