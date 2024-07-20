
class StudentProvider:
    studentuniform = "red"

    #constructor
    def __init__(self,name,rno):
        self.sname = name
        self.rollnum = rno
        self._srank = 100
        self.saddress = " default address"
    def display(self):
        print(self.sname, self.rollnum, self.saddress)
    def addAddress(self,address):
        self.saddress = address
    def getRank(self):
        return self._srank

class ExamProvider(StudentProvider):
    #constructor
    def __init__(self,name,rno,ecenter):
        super().__init__(name, rno)
        self.examcenter = ecenter
        self.location = "local"
    def moredisplay(self):
        print(super().getRank(), self.examcenter, self.location)