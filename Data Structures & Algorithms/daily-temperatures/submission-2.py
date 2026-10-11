class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)) :
            if not stack :
                stack.append(i)
            else :
                while stack and temperatures[stack[-1]] < temperatures[i] :
                    idx = stack.pop()
                    answer[idx] = i - idx
                
                stack.append(i)

        return answer