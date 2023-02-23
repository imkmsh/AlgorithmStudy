import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = list(range(n+1))
# print(parent)

def find(node):
    if node == parent[node]:
        return node
    else:
        root = find(parent[node])
        parent[node] = root
        return parent[node]


def union(a, b):
    if find(a) != find(b):
        parent[find(b)] = find(a)



for _ in range(m):
    q, a, b = map(int, input().split())

    if q == 0:
        union(a, b)
        # print(parent)

    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    # print(parent)
