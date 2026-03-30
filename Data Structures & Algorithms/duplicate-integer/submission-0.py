class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # set={}
        # set1,2,3
        # nums=1,2,3,3
        hashset=set()  # {1:0, 2:1, 3:2, 3:3}
        # {1,2,3}
        for i in range(len(nums)):
            if nums[i] in hashset: #1
                return True
            hashset.add(nums[i]) 
        return False

        ## o(n), o(n)
        # print(nums)
        # print(list(set(nums))
        # return len(nums)!=len(set(nums))