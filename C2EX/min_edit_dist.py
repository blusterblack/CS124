import numpy as np


class MinEditDistnace:
    def __init__(self, cost=[1, 1, 1]):
        self.cost = cost

    def findDistance(self, s1, s2):

        insert, delete, subt = self.cost
        l1, l2 = (len(s1), len(s2))
        a = np.zeros((l1, l2), int)
        align = np.zeros((l1, l2), str)

        a[0][0] = subt * (s1[0] != s2[0])
        for i in range(1, l1):
            a[i][0] = a[i-1][0]+1
        for i in range(1, l2):
            a[0][i] = a[0][i-1]+1
        for i in range(1, l1):
            for j in range(1, l2):
                up, diag, left = (a[i-1][j]+delete,
                                  a[i-1][j-1]+subt,
                                  a[i][j-1]+insert)
                cmin = min(up, diag, left)
                if s1[i] != s2[j]:
                    if up == cmin:
                        a[i][j] += up
                        align[i][j] = '^'
                    elif left == cmin:
                        a[i][j] = left
                        align[i][j] = '<'
                    else:
                        a[i][j] = diag
                else:
                    a[i][j] += a[i-1][j-1]

        return align


cal = MinEditDistnace(cost=[1, 1, 2])
print(cal.findDistance('intention', 'execution'))
