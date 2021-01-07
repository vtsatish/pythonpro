from Library import pylib

print('welcome to the world of: \n')

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))

print('Python')

print('\n stay strong and learn')

print(str(pylib.fileExists("Library/test_simple.txt")))



