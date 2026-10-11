class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x:x[0], reverse=True)

        stack = []
        answer = 0
        for pos, spd in cars :
            res = (target - pos) / spd

            if not stack :
                answer += 1
                stack.append(res)
            elif stack[-1] < res :
                answer += 1
                stack.append(res)
        return answer

# 0 , 2, 4
# 4,  2, 1

