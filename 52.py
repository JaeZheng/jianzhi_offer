"""
题目描述
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
"""

# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # s和pattern都为空
        if len(s)==0 and len(pattern)==0:
            return True
        # s不为空，pattern为空
        elif len(s)!=0 and len(pattern)==0:
            return False
        # s为空, pattern不为空
        elif len(s)==0 and len(pattern)!=0:
            # pattern中的第二位字符为*,则后移两位继续比较
            if len(pattern)>1 and pattern[1]=='*':
                return self.match(s, pattern[2:])
            else:  # 其他情况都不可以匹配
                return False
        # s和pattern都不为空
        else:
            # pattern第二个字符为*的情况
            if len(pattern)>1 and pattern[1]=='*':
                # s和pattern第一个元素不同，则s不变，pattern后移两位，相当于pattern前两位为空
                if s[0]!=pattern[0] and pattern[0]!='.':
                    return self.match(s, pattern[2:])
                else:
                    # 如果s[0]和pattern[0]相同且pattern第二个字符为*，这时有三种情况
                    # pattern后移两位,s不变；相当于pattern前两位视为空
                    # pattern后移两位,s后移一位；相当于pattern前两位与s第一位匹配
                    # pattern不变,s后移一位；相当于pattern前两位与s中多个位匹配
                    return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            # pattern第二个字符不为*的情况
            else:
                if s[0] == pattern[0] or pattern[0] == '.':
                    return self.match(s[1:], pattern[1:])
                else:
                    return False


s = "aaa"
pattern = "ab*a"
S = Solution()
result = S.match(s, pattern)
print(result)