import math

#Variables
patient_name = 'John'
patient_age = 30
is_registered = True

#print
print(patient_age, patient_name)

x = 1.9
test = 3

print(x + test)

print(len(patient_name))
print(patient_name.upper())

print(math.ceil(x))

#if condition
if patient_age > 1:
    print("Young guy")
elif patient_age > 10:
    print("Big guy")
else:
    print("Small")

#for loop
for num in range(1, 10, 3):
    print("Attempt", num, num * '.')
    print(f"Val is {num} and attempt {num + 1} times")

for char in patient_name:
    print(char)
