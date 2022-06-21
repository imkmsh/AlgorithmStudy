n = int(input())
words = []
for _ in range(n):
    words.append(int(input()))

# 1: 산술평균

ans1 = sum(words) / n
ans1 = round(ans1)
print(ans1)

# 2: 중앙값

words.sort()
ans2 = words[n // 2]
print(ans2)

# 3: 최빈값

ilist = [0] * 8001
for i in words:
    ilist[i + 4000] += 1

mosts = []
most = -1
for j in ilist:
    most += 1
    if j == max(ilist):
        mosts.append(most - 4000)
if len(mosts) > 1:
    mosts.sort()
    ans3 = mosts[1]
else:
    ans3 = ilist.index(max(ilist)) - 4000
print(ans3)

# 4: 범위

ans4 = max(words) - min(words)
print(ans4)