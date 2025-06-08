def LIP(pts):
    n = len(pts)
    ans = []
    for z in range(n):
        ans.append(0)
    for i in range(n):
        divcnt = 1
        tmp = []
        for z in range(n):
            tmp.append(0)
        tmp[0] = 1
        for j in range(n):
            if i != j:
                divcnt = divcnt * (pts[i][0] - pts[j][0])
                tmp2 = []
                for z in range(n):
                    tmp2.append(0)
                for k in range(n - 1):
                    tmp2[k + 1] = tmp[k]
                for k in range(n):
                    tmp[k] = (-1) * tmp[k] * pts[j][0]
                for k in range(n):
                    tmp[k] = tmp[k] + tmp2[k]
        for k in range(n):
            tmp[k] = tmp[k] * pts[i][1]
            tmp[k] = tmp[k] / divcnt
            ans[k] += tmp[k]
    def inner_res(x):
        res = 0
        for i in range(n):
            res += pow(x, i) * ans[i]
        return res
    return ans, inner_res
