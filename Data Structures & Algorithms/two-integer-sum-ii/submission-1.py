class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1

        ans = []
        while True :
            if left >= len(numbers) or right >= len(numbers) or left >= right : break
            sum = numbers[left] + numbers[right]
            if sum == target :
                ans.append(left + 1)
                ans.append(right + 1)
                break
            elif sum < target :
                left += 1
            else :
                right -= 1
        return ans
