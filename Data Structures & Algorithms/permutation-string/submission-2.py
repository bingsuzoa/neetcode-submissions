class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # answerList 세팅
        answerList = [0] * 26
        for s in s1 :
            answerList[ord(s) - ord('a')] += 1
        # left = 0
        left = 0

        # window = [0] * 26
        window = [0] * 26
        # for 문 돌리기
        for idx in range(len(s2)) :
            letter = s2[idx]
            right = ord(letter) - ord('a')
            # window[right] += 1
            window[right] += 1
            # right - left + 1 > len(s1) :
            if idx - left + 1 > len(s1) :
                # window[left] -= 1
                window[ord(s2[left]) - ord('a')] -= 1
                left += 1
            
            # if answerList == window :
            if answerList == window :
                return True
                # return True
        # return False
        return False

        