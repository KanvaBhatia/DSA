# https://leetcode.com/problems/sliding-window-maximum/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # if k == 1:
        #     return nums
        # res = [max(nums[0:k])]
        # l = 1
        # for r in range(k, len(nums)):
        #     if nums[r] > res[-1]:
        #         res.append(nums[r])
        #     elif nums[l - 1] == res[-1]:
        #         res.append(max(nums[l:r + 1]))
        #     else:
        #         res.append(res[-1])
        #     l += 1
        # return res
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
