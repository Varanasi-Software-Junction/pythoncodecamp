class Solution:
    def prefixCount(self, prefix):
        return len([x for x in arr if x.startswith(prefix)])

    def getPrefixes(self, arr):
        self.arr = arr
        prefixes = []
        for word in self.arr:
            prefix = ""
            for char in word:
                prefix = prefix + char
                n = self.prefixCount(prefix)
                if n == 1:
                    prefixes.append(prefix)
                    break
        return prefixes


arr = ["zebra", "dog", "duck", "dove"]
s = Solution()
print(s.getPrefixes(arr))
