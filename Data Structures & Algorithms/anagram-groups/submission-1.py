class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)

        for s in strs:
            count = [0] * 26 

            for char in s:
                count[ord(char) - ord("a")] += 1
            
            hash[tuple(count)].append(s)
        return list(hash.values())

        #  a - z (26) 

        #  array called count --> [a - z] = 1e, 1a, 1t

        #  hashmap: key[1e, 1t, 1a] : Value  
       