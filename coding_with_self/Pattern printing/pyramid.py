n = int(input("Enter the number of rows: "))
for i in range(n):
    # Print spaces before asterisks
    for j in range(n - i - 1):
        print(" ", end="")
    # Print asterisks
    for j in range(2 * i + 1):
        print("*", end="")
    print()  # Move to next line
