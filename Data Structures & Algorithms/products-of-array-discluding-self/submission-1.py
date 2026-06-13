from typing import List


def build_prefixes(nums):
    prefixes = []
    running_product = 1

    for number in nums:
        prefixes.append(running_product)
        running_product = running_product * number

    return prefixes


def build_postfixes(nums):
    postfixes = []
    running_product = 1

    for number in reversed(nums):
        postfixes.append(running_product)
        running_product = running_product * number

    postfixes.reverse()

    return postfixes


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        store = []

        prefixes = build_prefixes(nums)
        postfixes = build_postfixes(nums)

        for current_index in range(len(nums)):
            prefix = prefixes[current_index]
            postfix = postfixes[current_index]

            answer = prefix * postfix
            store.append(answer)

        return store


solution = Solution()
print(solution.productExceptSelf([1, 2, 4, 6]))
