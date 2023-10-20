rows = 5
for i in range(rows):
    for j in range(int((2*(rows-1) + 1)/2 - i)):
        print(" ", end = "")
    for j in range(2*i + 1):
        print("*", end = "")
    print()

for i in range(rows):
    for j in range(int((2*(rows-1) + 1)/2 - rows + 1 + i)):
        print(" ", end = "")
    for j in range(2 * rows - 1 - 2*i):
        print("*", end = "")
    print()
