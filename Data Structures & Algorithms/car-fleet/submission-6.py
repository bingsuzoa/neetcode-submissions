class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), key=lambda x:x[0], reverse= True)

        stack = []
        for pos, spd in cars :
            res = (target - pos) / spd
            if not stack or stack[-1] < res :
                stack.append(res)
        
        return len(stack)