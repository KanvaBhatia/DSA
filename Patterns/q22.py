out_num = 4
rows = out_num * 2 - 1

for i in range(rows):
    for j in range(rows):
        print(out_num - min(i, j, (2*out_num - 2) - j, (2*out_num - 2) - i), end = "")
    print()



# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444