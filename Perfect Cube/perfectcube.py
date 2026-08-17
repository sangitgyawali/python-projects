def is_perfect_cube(n):
    root = round(n ** (1/3))
    return root ** 3 == n

number = int(input("Enter a number:"))
if is_perfect_cube(number):
    print("Perfect cube")
else:
    print("Not a Perfect cube")
