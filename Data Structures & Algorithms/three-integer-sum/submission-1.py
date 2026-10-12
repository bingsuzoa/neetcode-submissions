class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answer = []
        for i in range(len(nums)) :
            target = -nums[i]
            
            left = i + 1
            right = len(nums) -1

            while True :
                if left >= right or left >= len(nums) : break
                result = nums[left] + nums[right]

                if  result == target :
                    if not [nums[i], nums[left], nums[right]] in answer :
                        answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif result < target :
                    left += 1
                else :
                    right -= 1
        
        return answer




