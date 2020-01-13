def comb(n,s="",a=0,b=0):
    if(a == b and a == n):
        print(s)
    if(a <= n):
        comb(n, s+"A", a+1, b)
        if(b < a):
            comb(n, s+"B", a, b+1)

n = int(input('Quantity of A(in grams):'))
comb(n)