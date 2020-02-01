"""
题目描述:
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
"""

# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        char_set = set(s)
        char_dict = {}
        for ch in char_set:
            char_dict[ch] = []
        for i in range(len(s)):
            char_dict[s[i]].append(i)
        for ch in s:
            if len(char_dict[ch]) == 1:
                return char_dict[ch][0]
        return -1


s = "aabcc"
S = Solution()
result = S.FirstNotRepeatingChar(s)
print(result)