class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmapS={} 
        hashmap={}
        for i in s:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        print(hashmap)
        # hashmap={r:2, a:2, c:2, e:1}

        for i in t:
            if i in hashmap:
                hashmap[i]-=1
                if hashmap[i] == 0:
                    del hashmap[i]
            else:
                return False
        return len(hashmap) == 0