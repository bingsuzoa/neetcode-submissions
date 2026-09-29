class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)) :
            if not stack :
                stack.append(i)
            else :
                if temperatures[stack[-1]] < temperatures[i] :
                    while stack and  temperatures[stack[-1]] <  temperatures[i] :
                        answer[stack[-1]] = i - stack[-1]
                        stack.pop()
                stack.append(i)
        
        return answer
        