class student:
    def __init__(self):
        college_name="XYZ"
        print("an instance is created", college_name)

    def getstudentData(self):
        print("will get student information")

student1=student()
student2=student()
student3=student()


student1.__init__()
student1.getstudentData()

