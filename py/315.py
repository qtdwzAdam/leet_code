"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
"""

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_nums = len(nums)
        if len_nums == 0: return []
        if len_nums == 1: return [0]
        res = []
        sum_nums = [nums[0]]
        for idx, val in enumerate(nums[1:]):
            sum_nums.append(sum_nums[idx] + val)
        for idx, val in enumerate(nums):
            print '\nstartnew'
            print val
            left = idx
            right = len_nums - 1
            now_idx = left
            now_sum = sum_nums[idx] + val
            print now_sum
            cnt_val = 0
            while right - left > 1:
                mid = (left + right) / 2
                print 'sss'
                print mid
                print now_sum
                print sum_nums[mid]
                print cnt_val
                if now_sum > sum_nums[mid]:
                    cnt_val += now_sum - left
                    left = mid
                else:
                    break
            res.append(cnt_val)

        return res



if __name__ == '__main__':
    sol = Solution()
    print sol.countSmaller([1])
    print sol.countSmaller([5, 2, 6, 1])
