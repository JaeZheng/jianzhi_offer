"""
题目描述:
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
解决思路：
把每行被1分割的两部分乘积都计算出来，这样可以从首尾分别用累乘算出两个列表，然后两个列表首尾相乘就是B的元素
"""

# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        head = [1]
        tail = [1]
        for i in range(len(A)-1):
            head.append(A[i]*head[i])
            tail.append(A[-i-1]*tail[i])
        return [head[j]*tail[-j-1] for j in range(len(A))]

A = [1,2,3,4,5]
S = Solution()
result = S.multiply(A)
print(result)