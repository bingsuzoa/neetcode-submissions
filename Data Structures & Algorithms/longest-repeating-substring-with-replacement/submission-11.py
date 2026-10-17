class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        graph = [0] * 26

        left = 0
        right = 0
        answer = 0
        while left <= right and right < len(s) :
            idx = ord(s[right]) - ord('A')
            graph[idx] += 1

            maxCount = max(graph)

            total = right - left + 1
            need = total - maxCount

            if need <= k :
                answer = max(answer, total)
                right += 1
            else :
                while left <= right :
                    idx = ord(s[left]) - ord('A')
                    graph[idx] -= 1
                    left += 1

                    maxCount = max(graph)
                    total = right - left + 1
                    need = total - maxCount

                    if need <= k :
                        break
                answer = max(answer, right - left + 1)    
                right += 1
        return answer
                