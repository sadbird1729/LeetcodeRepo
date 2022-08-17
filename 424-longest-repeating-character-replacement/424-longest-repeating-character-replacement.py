class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        nums = [0]*26
        left, right =0, 0
        res = 0
        while right<len(s):
            nums[ord(s[right])-ord('A')] += 1
            
            res = max(res,nums[ord(s[right])-ord('A')])
            if right-left+1-res>k:
                nums[ord(s[left])-ord('A')] -= 1
                left += 1
            right += 1
        return right - left
