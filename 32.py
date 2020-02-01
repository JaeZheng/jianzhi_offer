"""
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
解决思路：
第一种：
参考27题，先递归得到所有可能性的排列，然后把字典序排序第一个作为结果输出
第二种：
先把数组按字符组合后从小到大的顺序排列好，再转为拼接后的数字。
比较两个字符串s1, s2大小的时候，先将它们拼接起来，比较s1+s2,和s2+s1那个大，如果s1+s2大，那说明s2应该放前面，所以按这个规则，s2就应该排在s1前面。
通过一个双层遍历，把组合后能达到最小的数不断交换上去。
"""

# -*- coding:utf-8 -*-
# 第一种
# class Solution:
#     def PrintMinNumber(self, numbers):
#         if len(numbers) == 0:
#             return ""
#         numbers = [str(number) for number in numbers]
#         per = self.Permutation(numbers)
#         return int(per[0])
#
#     def Permutation(self, numbers):
#         if len(numbers) <= 1:
#             return numbers
#         res = set()
#         for i in range(len(numbers)):
#             for j in self.Permutation(numbers[:i]+numbers[i+1:]):
#                 res.add(numbers[i] + j)
#         return sorted(res)

# 第二种
class Solution:
    def PrintMinNumber(self, numbers):
        if len(numbers) == 0:
            return ""
        numbers = [str(number) for number in numbers]
        for i in range(len(numbers)-1):
            for j in range(i, len(numbers)):
                sum1 = int(numbers[i]+numbers[j])
                sum2 = int(numbers[j]+numbers[i])
                if sum2 < sum1:
                    tmp = numbers[j]
                    numbers[j] = numbers[i]
                    numbers[i] = tmp
        return int("".join(numbers))


S = Solution()
numbers = [3,32,321]
result = S.PrintMinNumber(numbers)
print(result)