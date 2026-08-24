class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = sorted(count, key=count.get, reverse=True)
        return result[:k]
