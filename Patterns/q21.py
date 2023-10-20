rows = 5

print("*" * rows)
for i in range(rows - 2):
    print('*', end = "")
    print(" " * (rows - 2), end = "")
    print('*', end = "")
    print()
print("*" * rows)

# *****
# *   *
# *   *
# *   *
# *****