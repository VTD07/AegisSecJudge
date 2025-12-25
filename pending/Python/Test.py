import sys

##############
sys.dont_write_bytecode = True
##############

sys.setrecursionlimit(10**7)

mod = 1209

def mu(a, n):
    if n == 0:
        return 1
    tam = mu(a, n // 2)
    tam = (tam * tam) % mod
    if n % 2 != 0:
        tam = (tam * a) % mod
    return tam

def cal(a, n):
    if n == 1:
        return a % mod
    tam = cal(a, n // 2)
    tam = (tam * (1 + mu(a, n // 2)) % mod) % mod
    if n % 2 != 0:
        tam = (tam + mu(a, n)) % mod
    return tam

a, n = map(int, input().split())
print(cal(a, n) + 1)