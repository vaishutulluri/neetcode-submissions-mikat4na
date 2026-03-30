class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        # res=[]
        for i, num in enumerate(nums):
            # 0,2
            if target-num in hashmap:
                return [hashmap[target-num],i]
            hashmap[num]=i