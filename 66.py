"""
题目描述:
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
解决思路：
将地图全部置1，遍历能够到达的点，将遍历的点置0并令计数+1.
这个思路在找前后左右相连的点很有用，比如leetcode中的海岛个数问题/最大海岛问题都可以用这种方法来求解。
"""

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0

    def movingCount(self, threshold, rows, cols):
        arr = [[1for j in range(cols)] for i in range(rows)]
        self.findWay(arr, threshold, 0, 0)
        return self.count

    def findWay(self, arr, threshold, i, j):
        # 保证不越界
        if i<0 or j<0 or i>=len(arr) or j>=len(arr[0]):
            return
        # 保证满足条件以及没有经过
        if self.numSum(i, j)>threshold or arr[i][j]!=1:
            return
        self.count += 1
        arr[i][j] = 0
        self.findWay(arr, threshold, i-1, j)
        self.findWay(arr, threshold, i+1, j)
        self.findWay(arr, threshold, i, j-1)
        self.findWay(arr, threshold, i, j+1)
        return

    def numSum(self, i, j):
        list_i = list(map(int, list(str(i))))
        list_j = list(map(int, list(str(j))))
        return sum(list_i) + sum(list_j)


i = 35
a = list(map(int, list(str(i))))
print(a)
