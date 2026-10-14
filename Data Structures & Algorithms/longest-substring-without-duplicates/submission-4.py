class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0

        answer = 0
        unique_set = set()
        while right < len(s) and left <= right :
            if not s[right] in unique_set :
                unique_set.add(s[right])
                answer = max(answer, right - left + 1)
                right += 1
            else :
                while s[right] in unique_set :
                    unique_set.remove(s[left])
                    left += 1
        
        return answer