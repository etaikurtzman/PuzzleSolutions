class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        k = []
        overall_max = 0
        for i in range(len(nums)):
            max = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    if k[j] > max:
                        max = k[j]
            k.append(max + 1)
            if k[i] > overall_max:
                overall_max = k[i]
        return overall_max