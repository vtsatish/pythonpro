import processMod
from ClassProvider import StudentProvider,ExamProvider

#wrong call
try:
    value = 10
    value = value + 'stringtext'
except:
    print("Wrong call")


# print even through func
print("Even numbers are : ", processMod.get_even_list(list(range(30))))

sa = StudentProvider("test student",1)
sa.display()
sa.rollnum = 2
sa.addAddress("ECC road, bangaluru")
sa.display()
print(sa.getRank())


ec = ExamProvider("new student",5,"hyd")
ec.display()
ec.moredisplay()


    