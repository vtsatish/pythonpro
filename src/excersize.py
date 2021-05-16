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
def even_print(max):
    for num in range(max):
        if (num+1) % 2 == 0:
            print("Even number", num+1)

# main
print(fizz_buzz(15))
even_print(60)

