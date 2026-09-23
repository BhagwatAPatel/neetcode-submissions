class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for num, i in count.items():
            if len(heap) <= k - 1:
                heapq.heappush(heap, (i, num))
            else: 
                heapq.heappush(heap, (i, num))
                heapq.heappop(heap)
        
        res = []
        for i, num in heap:
            res.append(num)
        return res