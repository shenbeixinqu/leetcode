# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。
#
#  示例1:
#
# 输入: 5
# 输出: True
# 解释: 1 * 1 + 2 * 2 = 5
#
#  示例2:
#
# 输入: 3
# 输出: False
#
#  Related Topics 数学


# leetcode submit region begin(Prohibit modification and deletion)
from math import sqrt


class Solution:
    def judgeSquareSum(self, c):
        assert c >= 0
        start, end = 0, int(sqrt(c))  # 设置头尾指针
        while start <= end:
            _sum = start ** 2 + end ** 2
            if _sum > c:
                end -= 1
            elif _sum < c:
                start += 1
            else:
                return True
        return False


result = Solution()
res = Solution.judgeSquareSum(12)

# leetcode submit region end(Prohibit modification and deletion)
