class student:
    count=0     # constructor
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        student.count=student.count+1       #class variable
    def displaystudentData(self):
        name= "sowmya"
        print("name",name)
        print("age", self.age)
        print("address", self.address)

student1=student("ram",22,"hyd")    # studenr1.  init  () internally invoked automatically
student2= student("sam",23,"pune")       # student2.  init  () internally
student3= student("soumya",21,"delhi")

print("no of student registered",student.count)
#student1.__init__()
student1.displaystudentData()
student2.displaystudentData()
student3.displaystudentData()

print(student1.__getattribute__('name'))
print(hasattr(student2,'age'))
print(hasattr(student2,'address'))
student2.displaystudentData()
setattr(student2,'age',20)
student2.displaystudentData()
print(getattr(student2,'address'))

print(__name__)
print(student.__name__)


