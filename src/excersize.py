def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizz and buzz"
    elif input % 5 == 0:
        return "buzz"
    elif input % 3 == 0:
        return "fizz"
    else:
        return input


# Print even numbers
max = 40
for num in range(max):
    if num % 2 == 0:
        print("Even number", num)

# main
print(fizz_buzz(15))
