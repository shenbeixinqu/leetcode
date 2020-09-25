# 和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
#
#  现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。
#
#  示例 1:
#
#
# 输入: [1,3,2,2,5,2,3,7]
# 输出: 5
# 原因: 最长的和谐数组是：[3,2,2,2,3].
#
#
#  说明: 输入的数组长度最大不超过20,000.
#  Related Topics 哈希表

"""
get()方法语法:
dict.get(key, default=None)
参数
    -key         字典中要查找的键
    -default     如果指定的键不存在时,返回该默认值
"""


class Solution:
    def findLHS(self, nums):
        dicts = {}
        res = 0
        for i in nums:
            dicts[i] = dicts.get(i, 0)+1
        for i in dicts:
            if i+1 in dicts:
                res = max(res, dicts[i]+dicts[i+1])
        print(res)
        return res


result = Solution()
res = result.findLHS([1, 4, 5, 7, 4, 3, 4, 5, 5, 5])
