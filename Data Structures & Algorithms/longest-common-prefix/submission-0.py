class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        #dance

        for i in range(1,len(strs)): #"dag","danger","damage"
            j=0
            while j < min(len(prefix), len(strs[i])): #0<3
                if prefix[j]!=strs[i][j]:
                    break
                j+=1 # Da
            prefix=prefix[0:j] #da
        return prefix

            





