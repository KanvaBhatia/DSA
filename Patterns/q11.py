rows = 5
init = True
for i in range(rows):
    prev = init
    for _ in range(i + 1):
        print(int(prev), end = "")
        prev = not prev
    init = not init
    print()

# 1
# 01
# 101
# 0101
# 10101