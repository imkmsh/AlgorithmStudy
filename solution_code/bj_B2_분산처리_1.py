n = int(input())
for _ in range(n):
    a, b = map(int,input().split())
    prd = 1
    for _ in range(b):
        prd = (prd * a)%10
    if prd == 0:
        print(10)
    else:
        print(prd)