# index1 < index2
# index1 + index2 = target
# index1 != index2
# 무조건 한번씩만 사용가능

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) -1
        res = numbers[left] + numbers[right]

        while True :
            if res > target :
                res -= numbers[right]
                right -= 1
                if right <= left : break
                res += numbers[right]
            elif res == target :
                return [left + 1, right + 1]
            else :
                res -= numbers[left]
                left += 1
                if right <= left : break
                res += numbers[left]

        return [0, 0]