# Quadratic time algo

# checking for disjointness
def disjoint(A, B, C):
    for a in A:
        for b in B:
            if a == b:
                for c in C
                    if a == c:
                        return False
    return True

# element uniqueness
def uniqueness1(S):
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False
    return True

# uniqueness 2
def uniqueness2(S):
    temp = sorted(S) # guarantees worst time O(n log n)
    for j in range(1, len(temp)):
        if S[j-1] == S[j]:
            return False
    return True
