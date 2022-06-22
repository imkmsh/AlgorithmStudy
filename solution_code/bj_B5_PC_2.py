n = int(input())

num_li = list(map(int, input().split()))
num_set = set(num_li)
ans = len(num_li) - len(num_set)

print(ans)
