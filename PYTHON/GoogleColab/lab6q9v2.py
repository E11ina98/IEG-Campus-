def pascal_triangle(m):
    a= [[] for i in range(m)]
    for i in range(m):
        for j in range(i+1):
            if (j<i):
                if (j==0):
                    a[i].append(1)
                else:
                    a[i].append(a[i-1][j]+a[i-1][j-1])
            elif(j==1):
                a[i].append(1)
    return a
m=5
print(pascal_triangle(m))

