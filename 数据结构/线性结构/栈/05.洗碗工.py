from pythonds3.basic import *
st = Stack()
s = input("请输入记录的顾客拿盘子的编号(一组)：")
n = 0
i = 0
while i < 10 and n < 10:
    k = int(s[i])
    if n <= k:
        for m in range(n, k + 1):
            st.push(m)
        n = k+1
    while not st.is_empty() and st.peek() == int(s[i]):
        m = int(st.pop())
        i += 1
if st.is_empty():
    print("YES")
else:
    print("NO")

















