import string, random
n = 32
l = string.ascii_letters + string.digits + '@#$%^&*'
m = len(l)
f = lambda x: random.randrange(x)
a = [l[f(m)] for _ in range(n)]
p = ''.join(a)
print(p)
    
