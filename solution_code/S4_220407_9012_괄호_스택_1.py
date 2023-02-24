n = int(input())


def vpc(string):
    front = []
    back = []
    for gh in string:
        if gh == '(':
            front.append(gh)
        elif gh == ')' and len(front) <= len(back):
            return 'NO'
        else:
            back.append(gh)
    if len(front) == len(back):
        return 'YES'
    else:
        return 'NO'


for i in range(n):
    res = vpc(input())
    print(res)

