# 자동차는 앞차를 추월할 수 없다. 따라잡은 다음에는 같은 속도로 움직일 뿐
# car fleet는 같은 위치, 같은 속도로 운전하는 집합. 자동차 1개도 집합으로 고려
# 차량이 차량 fleet의 목적지에 도착하는 순간 그 행렬에 합류한다면, 그 차량은 해당 차량 행렬의 일부로 간주
# 목적지에 도달하는 각각 다른 차량 fleet를 구하라

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        map = {}
        for i in range(len(position)) :
            map[position[i]] = i
        
        position = sorted(position, reverse = True)

        new_speed = []

        for n in position :
            idx = map[n]
            new_speed.append(speed[idx])

        
        stack = []
        for i in range(len(position)) :
            time = (target - position[i]) / new_speed[i]
            # print(f"{position[i]}, {time}")

            if stack and stack[-1] < time :
                stack.append(time)
            elif not stack :
                stack.append(time)
        
        return len(stack)
            

