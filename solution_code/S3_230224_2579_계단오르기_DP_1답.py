# 2579

num = int(input())
q = []
for i in range(num):
    q.append(int(input()))

# 10 20 15 25 10 20

# def ans(stair):
#     ans = stair[0]
#     score = [ans] * len(stair)
#     score[1] = stair[0] + stair[1]
#     score[2] = stair[0] + stair[2]
#     for i in range(2, len(stair)):
#         step1 = score[i-1]
#         step2 = score[i-2]
#         if step
#         score[i] += max(score[i-1], score[i-2])
#
# def ans(stair):
#     step = [0] * len(stair)
#     ways = [[1,1,0], [1,0,1], [0,1,0], [0,1,1]]
#     for i in range(len(step)):
#         if i == 0:
#             step[i] = 1
#         else:
#             if step[i-1] == 1 and step[i-2]==1:
#                 step[i] = 1

dp = [0] * len(q)
dp[0] = q[0]


ans = 0

if num == 1:
    ans = q[0]

else:
    dp[1] = q[0] + q[1]

    if num != 2:
        dp[2] = max(q[0] + q[2], q[1] + q[2])
        for i in range(3, len(q)):
            # print(dp)
            dp[i] = q[i] + max(dp[i - 2], dp[i - 3] + q[i - 1])
    ans = dp[-1]

print(ans)