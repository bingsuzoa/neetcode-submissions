class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alpa = [0] * 26
        left = 0
        maxFreq = 0
        answer = 0
        
        # for문
        for right in range(len(s)) :
            # 문자열의 idx 구하기
            idx = ord(s[right]) - ord('A')
            # alpa[idx] += 1
            alpa[idx] += 1
            # alpa의 maxFreq 구하기
            maxFreq = max(maxFreq, alpa[idx])
            # while (right - left + 1) - maxFreq > k :
            while (right - left + 1) - maxFreq > k :
                # left 빼고, left += 1
                idx = ord(s[left]) - ord('A')
                alpa[idx] -= 1
                left += 1
            # anwer 갱신
            answer = max(answer, right - left + 1)
        return answer