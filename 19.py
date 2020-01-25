"""
题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
解决思路：
第一种：设定上下左右四个边界，按顺时针顺序添加元素，并更新边界。
第二种：每次添加矩阵第一行，然后逆时针转置去掉第一行之后的矩阵，继续添加第一行
"""

# -*- coding:utf-8 -*-
# 第一种
# class Solution:
#     # matrix类型为二维列表，需要返回列表
#     def printMatrix(self, matrix):
#         if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
#             return []
#         up, down, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
#         result_list = []
#         while True:
#             # 最上面一行
#             for j in range(left, right+1):
#                 result_list.append(matrix[up][j])
#             # 向下逼近
#             up += 1
#             # 判断上下是否越界
#             if up > down:
#                 break
#             # 最右边一行
#             for i in range(up, down+1):
#                 result_list.append(matrix[i][right])
#             # 向左逼近
#             right -= 1
#             # 判断左右是否越界
#             if left > right:
#                 break
#             # 最下面一行
#             for j in range(right, left-1, -1):
#                 result_list.append(matrix[down][j])
#             # 向上逼近
#             down -= 1
#             # 判断上下是否越界
#             if up > down:
#                 break
#             # 最左边一行
#             for i in range(down, up-1, -1):
#                 result_list.append(matrix[i][left])
#             # 向右逼近
#             left += 1
#             # 判断左右是否越界
#             if left > right:
#                 break
#         return result_list

# 第二种
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        result_list = []
        while True:
            # 添加第一行
            result_list.extend(matrix[0])
            # 如果还有其他行，去掉第一行
            if len(matrix)>1:
                matrix = matrix[1::]
            else:
                break
            # 转置
            matrix = [[row[i] for row in matrix] for i in range(len(matrix[0])-1,-1,-1)]
        return result_list


S = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# matrix = [[1,2,3,4]]
result = S.printMatrix(matrix)
print(len(result))
print(result)