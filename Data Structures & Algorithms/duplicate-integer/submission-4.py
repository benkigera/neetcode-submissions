class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNumbers = set()

        for i in nums:
            if i in seenNumbers:
                return True
            seenNumbers.add(i)

        return False

solution = Solution()
print(solution.hasDuplicate([1, 2, 3, 3]))        