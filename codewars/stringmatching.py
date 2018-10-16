def solve(a, b):
    if a == b:
        return True
    found = False
    #     asterisk = a.index('*') if a.index('*') else None
    # This won't work because index will raise an error
    asterisk = None if not '*' in a else a.index('*')

    if asterisk is not None:
        sides = a.split('*')
        missing = b[len(sides[0]):len(b)-len(sides[1])]
        return a.replace('*', missing) == b

    return False


print(solve("code*s","codewars"))
# print(solve("codewar*s","codewars"))
print(solve("code*warrior","codewars"))
# print(solve("c","c"))
# print(solve("*s","codewars"))
# print(solve("*s","s"))
# print(solve("s*","s"))
# print(solve("aa","aaa") )
# print(solve("aa*","aaa"))
# print(solve("aaa","aa") )
# print(solve("aaa*","aa") )
# print(solve("*","codewars"))