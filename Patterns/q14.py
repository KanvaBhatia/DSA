# print(chr((65)))
rows = 5
for i in range(rows):
    for j in range(i + 1):
        print(chr(65 + j), end = "")
    print()

# A
# AB
# ABC
# ABCD
# ABCDE