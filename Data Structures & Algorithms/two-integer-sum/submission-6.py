class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans, hm = [], {}
        for idx, num in enumerate(nums):
            diff = target - num
            # If the difference is in the hasmap 
            if diff in hm:
                ans.append(hm[diff])
                ans.append(idx)
                return ans
            else: # Otherwise, add the curr value to hashmap
                hm[num] = idx
        return ans