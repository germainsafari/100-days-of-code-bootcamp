print("continue")
count = 0
while count < 5:
    count += 1
    if count == 3:
        break
    print(count)

print("this is the while loop")
count = 2
while count < 6:
    count += 1
    if count == 4:
        continue
    print(count)