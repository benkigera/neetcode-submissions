class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        most_frequent = counts.most_common(k)
        return [number for number, frequency in most_frequent]
