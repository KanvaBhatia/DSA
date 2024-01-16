# https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        sorted_keys = sorted(hashmap, key=lambda x: hashmap[x], reverse=True)
        return sorted_keys[:k]
