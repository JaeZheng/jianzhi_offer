"""
题目描述:
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
解决思路：
回溯法
"""

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.visited = []

    def hasPath(self, matrix, rows, cols, path):
        if not matrix:
            return False
        if len(path) == 0:
            return True
        self.visited = [False for _ in range(len(matrix))]
        for i in range(rows):
            for j in range(cols):
                if self.subPath(matrix, rows, cols, i, j, 0, path):
                    return True
        return False

    def subPath(self, matrix, rows, cols, i, j, index, s):
        if matrix[cols*i+j] != s[index] or self.visited[cols*i+j] == True:
            return False
        if index == len(s)-1:
            return True
        self.visited[cols * i + j] = True
        # 向上
        if i > 0 and self.subPath(matrix, rows, cols, i - 1, j, index + 1, s):
            return True
        # 向下
        if i < rows-1 and self.subPath(matrix, rows, cols, i + 1, j, index + 1, s):
            return True
        # 向左
        if j > 0 and self.subPath(matrix, rows, cols, i, j - 1, index + 1, s):
            return True
        # 向右
        if j < cols-1 and self.subPath(matrix, rows, cols, i, j + 1, index + 1, s):
            return True
        self.visited[cols * i + j] = False
        return False


s = "a b c e s f c s a d e e"
matrix = s.split(" ")
path = "abcb"
S = Solution()
result = S.hasPath(matrix, 3, 4, path)
print(result)