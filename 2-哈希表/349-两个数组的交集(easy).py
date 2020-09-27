# 给定两个数组，编写一个函数来计算它们的交集。
#
#
#  示例 1：
#
#  输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
#
#
#  示例 2：
#
#  输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
#
#
#  说明：
#
#  输出结果中的每个元素一定是唯一的。
#  我们可以不考虑输出结果的顺序。
#
#  Related Topics 排序 哈希表 双指针 二分查找


class Solution:
    def intersection(self, nums1, nums2):
        if not nums1 and not nums2:
            return []
        res = []
        hashmap1 = set(nums1)
        hashmap2 = set(nums2)
        for num in hashmap1:
            if num in hashmap2:
                res.append(num)
        print(res)
        return res


result = Solution()
res = result.intersection([1, 3, 5, 7], [4, 5, 6, 7, 8])


