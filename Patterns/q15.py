# print(chr((65)))
rows = 5
for i in range(rows):
    for j in range(rows - i):
        print(chr(65 + j), end = "")
    print()


# ABCDE
# ABCD
# ABC
# AB
# A