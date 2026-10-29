class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alpa = [0] * 26
        duSet = set()

        left = 0
        right = 0
        answer = 0

        while right < len(s):
            duSet.add(s[right])

            idx = ord(s[right]) - ord('A')
            alpa[idx] += 1

            if len(duSet) <= 1:
                answer = max(answer, right - left + 1)
                right += 1

            else:
                temp = self.getBig(alpa)
                A = (right - left + 1) - temp

                while A > k:
                    idx = ord(s[left]) - ord('A')
                    alpa[idx] -= 1

                    if alpa[idx] == 0:
                        duSet.remove(s[left])

                    left += 1

                    temp = self.getBig(alpa)
                    A = (right - left + 1) - temp

                answer = max(answer, right - left + 1)
                right += 1

        return answer

    def getBig(self, alpa):
        return max(alpa)