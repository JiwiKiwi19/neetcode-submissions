class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        in_degree = {}


        for word in words:
            for c in word:
                if c not in adj:
                    adj[c] = set()
                if c not in in_degree:
                    in_degree[c] = 0
        

        for i in range(len(words) - 1):
            word1, word2, = words[i], words[i+1]
            minLen = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            
            for c in range(minLen):
                c1, c2 = word1[c], word2[c]

                # c1 = t c2 = f
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        in_degree[c2] += 1

                    break
        

        queue = deque([c for c in in_degree if in_degree[c] == 0])
        res = []
        

        while queue:
            c = queue.popleft()
            res.append(c)
            for pekka in adj[c]:
                in_degree[pekka] -= 1
                if in_degree[pekka] == 0:
                    queue.append(pekka)

        #Khan Algo is a cycle detection

        if len(res) != len(in_degree):
            return ""
        
        return "".join(res)