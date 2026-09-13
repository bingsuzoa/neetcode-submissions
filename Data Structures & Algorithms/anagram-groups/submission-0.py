class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map정의
        data = {}
        # for문 돌리면서 단어 정렬
        for str in strs :
            value = ''.join(sorted(str))
            if value in data :
                data[value].append(str)
            else :
                data[value] = [str]

        return list(data.values())