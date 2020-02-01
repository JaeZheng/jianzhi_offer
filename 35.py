"""
题目描述:
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007
解决思路：
归并排序中，比较过程中当array[i]>array[j]时，会产生mid-i+1个逆序对。
在归并的过程中计算每个小区间的逆序对数，进而计算出大区间的逆序对数
"""

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.cnt = 0

    def InversePairs(self, data):
        if len(data) <= 1:
            return 0
        self.MergeSort(data, 0, len(data)-1)
        return self.cnt

    def MergeSort(self, array, start, end):
        if start < end:
            mid = int((start+end)/2)
            self.MergeSort(array, start, mid)
            self.MergeSort(array, mid+1, end)
            self.MergeOne(array, start, end, mid)
        else:
            return

    def MergeOne(self, array, start, end, mid):
        tmp = [0 for _ in range(end-start+1)]
        i, j, k = start, mid+1, 0
        while i<=mid and j<=end:
            if array[i] > array[j]:
                self.cnt = (self.cnt + mid - i + 1) % 1000000007
                tmp[k] = array[j]
                k += 1
                j += 1
            else:
                tmp[k] = array[i]
                k += 1
                i += 1
        while i<=mid:
            tmp[k] = array[i]
            k += 1
            i += 1
        while j<=end:
            tmp[k] = array[j]
            k += 1
            j += 1
        for l in range(k):
            array[start+l] = tmp[l]


data = [6,202,100,301,38,8,1]
S = Solution()
result = S.InversePairs(data)
print(result)