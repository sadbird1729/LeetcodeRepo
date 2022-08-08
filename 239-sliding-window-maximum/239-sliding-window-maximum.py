class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = collections.deque() # 单调队列，从大到小
        res = []
        for i in range(len(nums)):                
            # 保证从大到小 如果前面数小则需要依次弹出，直至满足要求
            while que and nums[que[-1]] <= nums[i]:
                que.pop()
            que.append(i)
            # 判断队首值是否有效
            if que[0] <= i-k:
                que.popleft()
            # 当窗口长度为k时 保存当前窗口中最大值
            if i+1 >= k:
                res.append(nums[que[0]])
        return res