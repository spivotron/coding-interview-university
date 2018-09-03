def findDiagonalOrder(self, matrix):
    result = []
    dd = collections.defaultdict(list)
    if not matrix: return result
