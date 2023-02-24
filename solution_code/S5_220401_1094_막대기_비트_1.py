x = int(input())

st = [64]

while(sum(st) > x):
    st.sort()
    min = st[0]
    st[0] = min / 2
    if sum(st) < x:
        st.append(min / 2)

print(len(st))