# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
#
#
#  示例:
#
#  给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
#  Related Topics 数组 哈希表


class Solution:
    def twoSum(self, nums, target):
        if not nums:
            return []
        # 需要返回坐标,采用字典形式的hashmap
        hash_map = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t not in hash_map:
                hash_map[nums[i]] = i
                print(hash_map)
            else:
                print(i, hash_map[t])
                return [i, hash_map[t]]

result = Solution()
res = result.twoSum([1, 5, 7, 4], 12)
