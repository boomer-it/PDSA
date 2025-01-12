def gcd(m,n):
    cf = [] # common factors list
    for i in range(1,min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            cf.append(i)
    return max(cf)
print(gcd(300,98))
