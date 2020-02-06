"""
题目描述:
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
解决思路：
第一种：用一个数组存储，计算时排序后输出中位数
"""

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data = []
    def Insert(self, num):
        self.data.append(num)
    def GetMedian(self, n=None):
        length = len(self.data)
        tmp_data = sorted(self.data)
        return tmp_data[int(length/2)] if length%2==1 else (tmp_data[int(length/2)]+tmp_data[int(length/2)-1])/2.0


flow = [5,2,3,4,1,6,7,0,8]
S = Solution()
result = []
for i in flow:
    S.Insert(i)
    result.append(S.GetMedian(0))
print(result)