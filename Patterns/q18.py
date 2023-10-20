rows = 5

for i in range(rows):
    for j in range(i + 1):
        print(chr(65 + rows - 1 - i + j), end = "")
    print()


# E
# DE
# CDE
# BCDE
# ABCDE
