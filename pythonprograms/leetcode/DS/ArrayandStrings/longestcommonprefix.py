def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or len(strs[0]) ==0:
            return ""
        for i in range(len(strs[0])): # use the first word as reference
            for j in range(1, len(strs)): # over the other words
                print(i)
                print(strs[j])
                print(strs[j][i])
                print(strs[0][i])
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

print(longestCommonPrefix(["flower","flow","flight"]))
