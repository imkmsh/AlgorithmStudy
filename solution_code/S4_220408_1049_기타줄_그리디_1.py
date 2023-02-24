def guitar(n, package, each):
    n_p = n // 6
    n_r = n % 6
    n_onlyp = n // 6 + 1
    price = min(n_onlyp * min(package),
                n_p * min(package) + n_r * min(each),
                n * min(each))
    return price


packs = []
eachs = []

n, m = tuple(map(int, input().split()))

for _ in range(m):
    a, b = tuple(map(int, input().split()))
    packs.append(a)
    eachs.append(b)

print(guitar(n, packs, eachs))
