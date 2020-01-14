def cal(n):
    if n==0:
        return 1
    return n*cal(n-1)
result=cal(7)
print(result)
