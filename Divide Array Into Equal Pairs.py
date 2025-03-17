
class Solution(object):
    def divideArray(self, nums):
        for i in set(nums):
            if nums.count(i)%2!=0:
                return False
        return True
       