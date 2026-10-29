class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duSet = set()
        left = 0
        right = 0
        answer = 0
        # right가 set에 있는지 확인
        while right < len(s) :
            if not s[right] in duSet :
                duSet.add(s[right])
                answer = max(answer, right - left + 1)
                right += 1
            else :
                while right < len(s) :
                    if not s[right] in duSet :
                        duSet.add(s[right])
                        answer = max(answer, right - left + 1)
                        right += 1
                    else :
                        duSet.remove(s[left])
                        left += 1
        return answer
            # 없으면 set에 추가 + 최대값갱신(right - left + 1) + 우측이동
            # 있으면 left에서 뺀다. 
                # right가 set에 있는지 확인.
                # 있으면 left에서 뺀다 반복
                # 없으면 right set에 추가 + 최대값갱신 +  우측이동