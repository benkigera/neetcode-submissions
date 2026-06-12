from typing import Counter


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            counter = Counter(word)
            # find the signature ... $ calculate the grouping key
            signature = tuple(sorted(counter.items()))

            # append each object under that key..
            if signature not in groups:
                # if key is not on our hashmap ... initialize it with an empty map ...
                groups[signature] = []
            groups[signature].append(word)

        return list(groups.values())


solution = Solution()
print(solution.groupAnagrams(strs=["act", "pots", "tops", "cat", "stop", "hat"]))
