class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duSet = set()

        for n in nums :
            if n in duSet :
                return True
            else :
                duSet.add(n)
        return False

    