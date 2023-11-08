n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

answer = []
for i in range(n):
    ans_row = []
    for j in range(n):
        aval = [data[i][j]]
        ans = -1
        for step in range(n):
            if i - step >= 0:
                aval.append(data[i - step][j])
            if i + step < n:
                aval.append(data[i + step][j])
            if j - step >= 0:
                aval.append(data[i][j - step])
            if j + step < n:
                aval.append(data[i][j + step])
            key = min(aval)

            if key < data[i][j]:
                ans = key
                break

            aval = [data[i][j]]

        ans_row.append(ans)
    answer.append(ans_row)

for i in range(n):
    print(*answer[i])