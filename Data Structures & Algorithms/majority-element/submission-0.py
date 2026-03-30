class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       hashmap={}
       n=len(nums)//2
       print(n)
       nums=sorted(nums)
       return nums[n]
    

    #    5:4, 1:3

    #    4/2 3/2
    #    4/2->5


