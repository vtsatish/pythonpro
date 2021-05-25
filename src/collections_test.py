import os
import time
from pip._vendor.distlib._backport.tarfile import _FileInFile
#functions
def list_test():
    list_var = [20, 40, 60, 80]
    print(list_var)
    print(list_var[0])
    list_var.remove(60)
    print(list_var)
    #list for loop
    for item in list_var:
        print("item is ",item)
    
def dict_test():
    states = { 'MS' : 'Mississippi', 'VA' : 'Virginia', 'AL' : 'Alabama', 'DC' : 'Washington' }
    classLevel = { 0 : 'Freshman', 1 : 'Sophomore', 2 : 'Junior', 3: 'Senior' }
    print(states)
    print(states['MS'])
    print(classLevel[0])
    #dict for loop
    for key in states:
        print(key)
        print(states[key])
def files_test():
    filepath = "newfile.txt"
    outfile = open(filepath,"w")
    students = {'R' : 'Rajesh', 'S' : 'Satish', 'A' : 'Aravind' }
    #create file and write dict in to file
    for key in students:
        outstr = key + " : " + students[key] + "\n"
        outfile.write(outstr)
    outfile.close()
    #read file and print
    infile = open(filepath, "r")
    for line in infile:
        print(line.rstrip())
    infile.close()
    time.sleep(5)
    #delete file
    os.remove(filepath)
    
    
       
#main program
list_test()
dict_test()
files_test()