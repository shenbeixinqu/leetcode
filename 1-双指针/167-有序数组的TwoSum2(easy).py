# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
#
#  函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
#
#  说明:
#
#
#  返回的下标值（index1 和 index2）不是从零开始的。
#  你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
#
#
#  示例:
#
#  输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
#  Related Topics 数组 双指针 二分查找

"""
解题思路:
由于数组是有序数组,利用头尾指针进行处理.头尾元素之和大于目标值,尾指针向前移动
如果大于目标值,尾指针向后移动
    1.先判断输入数组是否为空
    2.设置收尾指针分别指向首尾元素
    3.判断首尾指针对应的元素之和和目标值之间的关系
        i.如果大于目标值:尾指针前移,继续判断
        ii.如果小于目标值:头指针后移,继续判断
        iii.等于目标值:返回头尾指针(题目要求从1开始,因此首尾指针均需要加1)
"""


class Solution:
    def two_sum(self, numbers, target):
        if not numbers:
            return []
        start, end = 0, len(numbers)-1  # 头尾指针
        while start < end:
            _sum = numbers[start] + numbers[end]
            if _sum < target:
                start += 1
            elif _sum > target:
                end -= 1
            else:
                return [start+1, end+1]
        return []


result = Solution()
res = result.two_sum([1, 5, 7, 10], 12)
