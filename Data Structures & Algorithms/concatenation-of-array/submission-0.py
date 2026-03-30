class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [*nums, *nums] #o(n+n)
#1
#nums
#[nums, nums]