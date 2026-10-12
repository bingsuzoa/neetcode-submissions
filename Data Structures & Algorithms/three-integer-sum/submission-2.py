class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        answer = []

        for i in range(len(nums)):
            target = -nums[i]

            if i > 0 and nums[i] == nums[i-1] : continue

            left = i + 1
            right = len(nums) -1

            while left < right :
                result = nums[left] + nums[right]

                if result == target :
                    answer.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left -1] :
                        left += 1
                    while left < right and nums[right] == nums[right +1] :
                        right -= 1
                elif result < target :
                    left += 1
                else :
                    right -= 1
        return answer