# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
#
#  示例 1：
#
#  输入："hello"
# 输出："holle"
#
#
#  示例 2：
#
#  输入："leetcode"
# 输出："leotcede"
#
#
#  提示：
#
#  元音字母不包含字母 "y" 。
#
#  Related Topics 双指针 字符串


class Solution:
    def reverseVowels(self, s):
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowel_reversed = []

        for i in range(len(s)):
            if s[i] in vowel:
                vowel_reversed.append([s[i], i])

        for j in range(len(vowel_reversed) // 2):
            vowel_reversed[j][0], vowel_reversed[len(vowel_reversed) - j - 1][0] = \
            vowel_reversed[len(vowel_reversed) - j - 1][0], vowel_reversed[j][0]

        list_s = list(s)
        for k in vowel_reversed:
            list_s[k[1]] = k[0]

        return "".join(list_s)

result = Solution()
res = result.reverseVowels('supopport')
