class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniSet = set()

        left = 0
        right = 0
        answer = 0

        while left <= right and right < len(s) :
            if not s[right] in uniSet :
                uniSet.add(s[right])
                answer = max(answer, right - left + 1)
                right += 1
            else :
                while s[right] in uniSet :
                    uniSet.remove(s[left])
                    left += 1
        return answer 
