rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end = "")
    for k in range(2 * (rows - i)):
        print(" ", end = "")
    for l in range(i, 0, -1):
        print(l, end = "")
    print()
        
# 1      1
# 12    21
# 123  321
# 12344321
