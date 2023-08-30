# def walk(steps):
#     for step in range(1, steps +1):
#         print(step)
# walk(6)

def walk(steps):
    if steps == 0:
        quit()
    walk(steps - 2)
    print(f"you walked{steps}")
walk(20)