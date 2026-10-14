class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        graph = [0] * 26

        map = {
            'A' : 0,
            'B' : 1,
            'C' : 2,
            'D' : 3,
            'E' : 4,
            'F' : 5,
            'G' : 6,
            'H' : 7,
            'I' : 8,
            'J' : 9,
            'K' : 10,
            'L' : 11,
            'M' : 12,
            'N' : 13,
            'O' : 14,
            'P' : 15,
            'Q' : 16,
            'R' : 17,
            'S' : 18,
            'T' : 19,
            'U' : 20,
            'V' : 21,
            'W' : 22,
            'X' : 23,
            'Y' : 24,
            'Z' : 25
        }

        left = 0
        right = 0
        answer = 0
        while left <= right and right < len(s) :
            idx = map[s[right]]
            graph[idx] += 1

            maxCount = 0
            for n in graph :
                maxCount = max(maxCount, n)
            
            length = right - left + 1
            need = length - maxCount

            if need <= k :
                answer = max(answer, right - left + 1)
                right += 1
            else :
                while need > k :
                    mIdx = map[s[left]]
                    graph[mIdx] -=1
                    left += 1

                    for n in graph :
                        maxCount = max(maxCount, n)
                    
                    length = right - left + 1
                    need = length - maxCount
                right += 1
        return answer

