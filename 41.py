"""
题目描述:
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
解决思路：
第一种：双层循环遍历穷举
第二种：双指针滑窗
"""

# -*- coding:utf-8 -*-
# 第一种
# class Solution:
#     def FindContinuousSequence(self, tsum):
#         result = []
#         for i in range(1, tsum):
#             tmp = i
#             if tmp == tsum:
#                 result.append([tmp])
#             for j in range(i+1, tsum):
#                 tmp += j
#                 if tmp < tsum:
#                     continue
#                 elif tmp > tsum:
#                     break
#                 else:
#                     result.append([k for k in range(i,j+1)])
#                     break
#         return result

# 第二种
class Solution:
    def FindContinuousSequence(self, tsum):
        result = []
        if tsum <= 0:
            return result
        elif 0<tsum<=2:
            return [tsum]
        ptr1, ptr2 = 1, 2
        sum = ptr1 + ptr2
        while tsum > ptr2:
            if sum < tsum:
                ptr2 += 1
                sum += ptr2
            elif sum > tsum:
                sum -= ptr1
                ptr1 += 1
            else:
                result.append([i for i in range(ptr1, ptr2+1)])
                ptr2 += 1
                sum += ptr2
        return result


tsum = 100
S = Solution()
result = S.FindContinuousSequence(tsum)
print(result)