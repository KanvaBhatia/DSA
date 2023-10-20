rows = 5
for i in range(rows):
    for j in range(rows - i):
        print(" ", end = "")
    for k in range(i + 1):
        print(chr(65 + k), end = "")
    for l in range(i, 0, -1):
        print(chr(65 + l - 1), end = "")
    print()

#      A
#     ABA
#    ABCBA
#   ABCDCBA
#  ABCDEDCBA