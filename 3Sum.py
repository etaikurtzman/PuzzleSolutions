class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()
        for i in range(len(nums) - 2):
            a = nums[i]
            if not(i > 0 and a == nums[i - 1]):
                left = i + 1
                right = len(nums) - 1
                
                while (left < right):
                    threesum = a + nums[left] + nums[right]
                    if threesum > 0:
                        right = right - 1
                    elif threesum < 0:
                        left = left + 1
                    else:
                        sol.append([nums[i],nums[left],nums[right]])
                        right = right - 1
                        while nums[right] == nums[right + 1] and left < right:
                            right = right - 1
        return sol