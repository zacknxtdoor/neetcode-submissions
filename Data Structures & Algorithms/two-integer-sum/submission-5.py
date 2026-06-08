class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans, hm = [], {}
        for idx, num in enumerate(nums):
            diff = target - num
            # If the difference isn't in the hasmap already
            if not (diff in hm):
                hm[num] = idx # add it
            else: # But if we find the difference of the target and 
                  # curr value, idx of the diff and our curr value
                  # are the solutions
                ans.append(hm[diff])
                ans.append(idx)
        return ans