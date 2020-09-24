# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
#  说明：本题中，我们将空字符串定义为有效的回文串。
#
#  示例 1:
#
#  输入: "A man, a plan, a canal: Panama"
# 输出: true
#
#  示例 2:
#
#  输入: "race a car"
# 输出: false
#
#  Related Topics 双指针 字符串
#  👍 278 👎 0


# Python isalnum() 方法检测字符串是否由字母和数字组成。
class Solution:
    def isPalindrome(self, s):
        if len(s) <= 1:
            return True
        start, end = 0, len(s) - 1
        while start < end:
            if s[start].isalbum() and s[end].isalbum():
                if s[start].lower() == s[end].lower():
                    start += 1
                    end -= 1
                    continue
                else:
                    return False
            elif s[start].isalbum():
                end -= 1
            elif s[end].isalbum():
                start += 1
            else:
                start += 1
                end -= 1
        return True