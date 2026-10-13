class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        u_set = set()

        left = 0
        right = 0

        answer = 0
        while left <= right and right < len(s) :
            if not s[right] in u_set :
                answer = max(answer, right - left + 1)
                u_set.add(s[right])
                right += 1
            else :
                if s[left] in u_set :
                    u_set.remove(s[left])
                    left += 1

        return answer