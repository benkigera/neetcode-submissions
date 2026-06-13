from math import prod


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        store = []
        for current_index in range(len(nums)):
            # give me all numbers before current index
            prefix_numbers = nums[:current_index]
            # give me all numbers after current index
            postfix_numbers = nums[current_index + 1 :]
            prefix = prod(prefix_numbers)
            postfix = prod(postfix_numbers)
            print(prefix)

            answer = prefix * postfix
            store.append(answer)
        return store
