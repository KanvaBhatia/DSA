rows = 10
for i in range(int(rows/2)):
    print("*" * int((rows - 2 * i) / 2), end = "")
    print(" " * 2 * i, end = "")
    print("*" * int((rows - 2 * i) / 2), end = "")
    if i != int(rows/2) - 1: print()
for i in range(int(rows/2), 0 - 1, -1):
    print("*" * int((rows - 2 * i) / 2), end = "")
    print(" " * 2 * i, end = "")
    print("*" * int((rows - 2 * i) / 2))


# **********
# ****  ****
# ***    ***
# **      **
# *        *          
# *        *
# **      **
# ***    ***
# ****  ****
# **********
