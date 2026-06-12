class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        print(counts)
        most_frequent = counts.most_common(k)
        print(most_frequent)
        return [number for number, frequency in most_frequent]
