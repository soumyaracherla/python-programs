class student:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def displaystudentData(self):
        name= "sowmya"
        print("name",name)
        print("age", self.age)
        print("address", self.address)

student1=student("ram",22,"hyd")    # studenr1.  init  () internally invoked automatically
# student2= student()       # student2.  init  () internally


#student1.__init__()
student1.displaystudentData()




